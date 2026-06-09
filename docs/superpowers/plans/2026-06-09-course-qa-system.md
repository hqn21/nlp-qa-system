# Course QA System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a vision-first RAG system that reads a 2-column CSV of questions and fills in short, precise answers grounded in fixed course slide PDFs.

**Architecture:** Offline (untimed) indexing renders each slide page to an image, transcribes it to markdown with GPT-5.5, semantically re-chunks with GPT-5.5, embeds with text-embedding-3-large, and persists a layered content-hash cache (FAISS dense + BM25 sparse). Online (timed) query does hybrid retrieval (RRF) → GPT-5.5 listwise rerank → GPT-5.5 answer generation, parallelized across questions.

**Tech Stack:** Python 3.12, uv, `openai`, `pymupdf`, `faiss-cpu`, `rank-bm25`, `jieba`, `numpy`, `pytest`.

---

## File Structure

```
src/nlp_qa_system/
  config.py              # Config dataclass + model-name constants
  openai_client.py       # OpenAIClient: complete() / embed() with retry
  io/csv_io.py           # read_questions() / write_answers()
  indexing/
    pdf_render.py        # render_pdf(): PDF -> list[png bytes]
    vision_parse.py      # parse_page(): image -> markdown (GPT-5.5)
    chunk.py             # Chunk dataclass + semantic_chunks() (GPT-5.5)
    embed.py             # embed_texts(): texts -> np.ndarray
    cache.py             # file_sha256, load/save manifest, save/load chunks
    build_index.py       # build_index() + load_index()
  retrieval/
    dense.py             # DenseIndex (FAISS IndexFlatIP, cosine)
    sparse.py            # tokenize() + BM25Index
    hybrid.py            # rrf_fuse()
    rerank.py            # rerank() listwise (GPT-5.5)
  qa/
    answer.py            # generate_answer() (GPT-5.5)
    pipeline.py          # answer_question() + run_batch()
  __main__.py            # CLI: `index` / `run --input --output`
tests/
  conftest.py            # FakeClient + shared fixtures
  ... mirrors src layout
```

Interfaces shared across tasks (defined once, reused verbatim):

- `OpenAIClient.complete(messages: list[dict], model: str, temperature: float = 0.0) -> str`
- `OpenAIClient.embed(texts: list[str], model: str) -> list[list[float]]`
- `Chunk(chunk_id: str, deck: str, text: str)`
- `DenseIndex.search(query: np.ndarray, top_n: int) -> list[tuple[int, float]]`
- `BM25Index.search(query: str, top_n: int) -> list[tuple[int, float]]`
- `rrf_fuse(rankings: list[list[int]], k: int = 60) -> list[tuple[int, float]]`
- `rerank(client, query: str, candidates: list[str], model: str, top_k: int) -> list[int]`
- `generate_answer(client, question: str, contexts: list[str], model: str, temperature: float = 0.0) -> str`

All LLM/embedding access goes through an injected `client` exposing `complete`/`embed`, so tests pass a `FakeClient` and never hit the network.

---

## Task 0: Project setup

**Files:**
- Modify: `pyproject.toml`
- Create: `tests/__init__.py`, `tests/conftest.py`
- Create package dirs: `src/nlp_qa_system/{io,indexing,retrieval,qa}/__init__.py`

- [ ] **Step 1: Add dependencies**

Run:
```bash
uv add openai pymupdf faiss-cpu rank-bm25 jieba numpy
uv add --dev pytest
```

- [ ] **Step 2: Create package subdirectories**

```bash
mkdir -p src/nlp_qa_system/io src/nlp_qa_system/indexing src/nlp_qa_system/retrieval src/nlp_qa_system/qa tests
touch src/nlp_qa_system/io/__init__.py src/nlp_qa_system/indexing/__init__.py src/nlp_qa_system/retrieval/__init__.py src/nlp_qa_system/qa/__init__.py tests/__init__.py
```

- [ ] **Step 3: Create the shared FakeClient fixture**

Create `tests/conftest.py`:
```python
class FakeClient:
    """Stand-in for OpenAIClient. complete() pops from a queue; embed() maps text->vector."""

    def __init__(self, complete_responses=None, embeddings=None, default_dim=4):
        self._completes = list(complete_responses or [])
        self._embeddings = dict(embeddings or {})
        self._default_dim = default_dim
        self.calls = []

    def complete(self, messages, model, temperature=0.0):
        self.calls.append(("complete", model))
        return self._completes.pop(0)

    def embed(self, texts, model):
        self.calls.append(("embed", model))
        return [self._embeddings.get(t, [0.0] * self._default_dim) for t in texts]
```

- [ ] **Step 4: Verify pytest runs**

Run: `uv run pytest -q`
Expected: `no tests ran` (exit 0), no import errors.

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml uv.lock src/nlp_qa_system tests
git commit -m "chore: add deps and test scaffolding"
```

---

## Task 1: config.py

**Files:**
- Create: `src/nlp_qa_system/config.py`
- Test: `tests/test_config.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
from nlp_qa_system.config import Config, EMBED_MODEL, ANSWER_MODEL

def test_config_defaults():
    c = Config()
    assert c.top_n == 20
    assert c.top_k == 6
    assert c.rrf_k == 60
    assert c.query_concurrency == 8
    assert c.index_dir == Path("data/index")
    assert EMBED_MODEL == "text-embedding-3-large"
    assert ANSWER_MODEL == "gpt-5.5"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_config.py -v`
Expected: FAIL with `ModuleNotFoundError: nlp_qa_system.config`

- [ ] **Step 3: Write minimal implementation**

```python
from dataclasses import dataclass
from pathlib import Path

VISION_MODEL = "gpt-5.5"
CHUNK_MODEL = "gpt-5.5"
RERANK_MODEL = "gpt-5.5"
ANSWER_MODEL = "gpt-5.5"
EMBED_MODEL = "text-embedding-3-large"


@dataclass(frozen=True)
class Config:
    slides_dir: Path = Path("docs/slides")
    index_dir: Path = Path("data/index")
    render_dpi: int = 180
    top_n: int = 20
    top_k: int = 6
    rrf_k: int = 60
    query_concurrency: int = 8
    index_concurrency: int = 8
    max_retries: int = 5
    answer_temperature: float = 0.0
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_config.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/config.py tests/test_config.py
git commit -m "feat: add config with model constants and defaults"
```

---

## Task 2: io/csv_io.py

**Files:**
- Create: `src/nlp_qa_system/io/csv_io.py`
- Test: `tests/io/test_csv_io.py`

- [ ] **Step 1: Write the failing test**

Create `tests/io/__init__.py` (empty) and `tests/io/test_csv_io.py`:
```python
from pathlib import Path
from nlp_qa_system.io.csv_io import read_questions, write_answers

def test_read_questions_two_columns_no_header(tmp_path: Path):
    p = tmp_path / "in.csv"
    p.write_text("什麼是 transformer?,\nWhat is BM25?,\n", encoding="utf-8")
    assert read_questions(p) == ["什麼是 transformer?", "What is BM25?"]

def test_read_skips_blank_rows(tmp_path: Path):
    p = tmp_path / "in.csv"
    p.write_text("Q1,\n\n,\nQ2,\n", encoding="utf-8")
    assert read_questions(p) == ["Q1", "Q2"]

def test_read_handles_bom(tmp_path: Path):
    p = tmp_path / "in.csv"
    p.write_text("Q1,\n", encoding="utf-8-sig")
    assert read_questions(p) == ["Q1"]

def test_write_answers_roundtrip_preserves_order_and_quoting(tmp_path: Path):
    out = tmp_path / "out.csv"
    write_answers(out, ["Q1", 'Has, comma'], ["A1", 'multi\nline'])
    # read back via csv to confirm valid quoting
    import csv
    with open(out, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert rows == [["Q1", "A1"], ["Has, comma", "multi\nline"]]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/io/test_csv_io.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
import csv
from pathlib import Path


def read_questions(path: Path) -> list[str]:
    questions: list[str] = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            if not row:
                continue
            q = row[0].strip()
            if q:
                questions.append(q)
    return questions


def write_answers(path: Path, questions: list[str], answers: list[str]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for q, a in zip(questions, answers):
            writer.writerow([q, a])
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/io/test_csv_io.py -v`
Expected: PASS (4 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/io/csv_io.py tests/io
git commit -m "feat: add CSV read/write (no header, 2 cols, BOM, quoting)"
```

---

## Task 3: retrieval/sparse.py (jieba + BM25)

**Files:**
- Create: `src/nlp_qa_system/retrieval/sparse.py`
- Test: `tests/retrieval/test_sparse.py`

- [ ] **Step 1: Write the failing test**

Create `tests/retrieval/__init__.py` (empty) and `tests/retrieval/test_sparse.py`:
```python
from nlp_qa_system.retrieval.sparse import tokenize, BM25Index

def test_tokenize_mixed_language_lowercases():
    toks = tokenize("Transformer 是一種 NLP 模型")
    assert "transformer" in toks
    assert "nlp" in toks

def test_bm25_ranks_relevant_doc_first():
    docs = [
        "BM25 是一種詞頻排序演算法",
        "transformer 使用 self-attention",
        "cipher decryption 與密碼學",
    ]
    idx = BM25Index.build(docs)
    hits = idx.search("self-attention transformer", top_n=3)
    assert hits[0][0] == 1

def test_bm25_save_load_roundtrip(tmp_path):
    idx = BM25Index.build(["alpha beta", "gamma delta"])
    p = tmp_path / "bm25.pkl"
    idx.save(p)
    loaded = BM25Index.load(p)
    assert loaded.search("gamma", top_n=1)[0][0] == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/retrieval/test_sparse.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
import pickle
from pathlib import Path

import jieba
from rank_bm25 import BM25Okapi


def tokenize(text: str) -> list[str]:
    return [t for t in jieba.lcut(text.lower()) if t.strip()]


class BM25Index:
    def __init__(self, bm25: BM25Okapi):
        self._bm25 = bm25

    @classmethod
    def build(cls, texts: list[str]) -> "BM25Index":
        tokenized = [tokenize(t) for t in texts]
        return cls(BM25Okapi(tokenized))

    def search(self, query: str, top_n: int) -> list[tuple[int, float]]:
        scores = self._bm25.get_scores(tokenize(query))
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return [(i, float(scores[i])) for i in ranked[:top_n]]

    def save(self, path: Path) -> None:
        with open(path, "wb") as f:
            pickle.dump(self._bm25, f)

    @classmethod
    def load(cls, path: Path) -> "BM25Index":
        with open(path, "rb") as f:
            return cls(pickle.load(f))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/retrieval/test_sparse.py -v`
Expected: PASS (3 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/retrieval/sparse.py tests/retrieval
git commit -m "feat: add BM25 sparse index with jieba tokenization"
```

---

## Task 4: retrieval/dense.py (FAISS cosine)

**Files:**
- Create: `src/nlp_qa_system/retrieval/dense.py`
- Test: `tests/retrieval/test_dense.py`

- [ ] **Step 1: Write the failing test**

```python
import numpy as np
from nlp_qa_system.retrieval.dense import DenseIndex

def test_dense_returns_nearest_first():
    emb = np.array([[1.0, 0.0], [0.0, 1.0], [0.9, 0.1]], dtype="float32")
    idx = DenseIndex.build(emb)
    hits = idx.search(np.array([1.0, 0.0], dtype="float32"), top_n=2)
    assert [i for i, _ in hits] == [0, 2]

def test_dense_save_load_roundtrip(tmp_path):
    emb = np.array([[1.0, 0.0], [0.0, 1.0]], dtype="float32")
    p = tmp_path / "index.faiss"
    DenseIndex.build(emb).save(p)
    loaded = DenseIndex.load(p)
    assert loaded.search(np.array([0.0, 1.0], dtype="float32"), top_n=1)[0][0] == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/retrieval/test_dense.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
from pathlib import Path

import faiss
import numpy as np


class DenseIndex:
    def __init__(self, index: "faiss.Index"):
        self._index = index

    @classmethod
    def build(cls, embeddings: np.ndarray) -> "DenseIndex":
        emb = np.ascontiguousarray(embeddings, dtype="float32").copy()
        faiss.normalize_L2(emb)
        index = faiss.IndexFlatIP(emb.shape[1])
        index.add(emb)
        return cls(index)

    def search(self, query: np.ndarray, top_n: int) -> list[tuple[int, float]]:
        q = np.ascontiguousarray(query, dtype="float32").reshape(1, -1).copy()
        faiss.normalize_L2(q)
        scores, ids = self._index.search(q, top_n)
        return [(int(i), float(s)) for i, s in zip(ids[0], scores[0]) if i != -1]

    def save(self, path: Path) -> None:
        faiss.write_index(self._index, str(path))

    @classmethod
    def load(cls, path: Path) -> "DenseIndex":
        return cls(faiss.read_index(str(path)))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/retrieval/test_dense.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/retrieval/dense.py tests/retrieval/test_dense.py
git commit -m "feat: add FAISS dense index (cosine via normalized IP)"
```

---

## Task 5: retrieval/hybrid.py (RRF)

**Files:**
- Create: `src/nlp_qa_system/retrieval/hybrid.py`
- Test: `tests/retrieval/test_hybrid.py`

- [ ] **Step 1: Write the failing test**

```python
from nlp_qa_system.retrieval.hybrid import rrf_fuse

def test_rrf_rewards_items_high_in_both_rankings():
    dense = [2, 0, 1]
    sparse = [0, 2, 3]
    fused = rrf_fuse([dense, sparse], k=60)
    order = [i for i, _ in fused]
    assert order[0] in (0, 2)  # appears near top of both
    assert set(order) == {0, 1, 2, 3}

def test_rrf_scores_descending():
    fused = rrf_fuse([[0, 1], [1, 0]], k=60)
    scores = [s for _, s in fused]
    assert scores == sorted(scores, reverse=True)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/retrieval/test_hybrid.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
def rrf_fuse(rankings: list[list[int]], k: int = 60) -> list[tuple[int, float]]:
    scores: dict[int, float] = {}
    for ranking in rankings:
        for rank, idx in enumerate(ranking):
            scores[idx] = scores.get(idx, 0.0) + 1.0 / (k + rank + 1)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/retrieval/test_hybrid.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/retrieval/hybrid.py tests/retrieval/test_hybrid.py
git commit -m "feat: add RRF fusion for hybrid retrieval"
```

---

## Task 6: openai_client.py (retry wrapper)

**Files:**
- Create: `src/nlp_qa_system/openai_client.py`
- Test: `tests/test_openai_client.py`

- [ ] **Step 1: Write the failing test**

```python
import pytest
from nlp_qa_system.openai_client import OpenAIClient

def test_retry_succeeds_after_transient_failures():
    client = OpenAIClient.__new__(OpenAIClient)  # bypass __init__/network
    client.max_retries = 5
    client.backoff_base = 0.0
    calls = {"n": 0}

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise RuntimeError("rate limited")
        return "ok"

    assert client._retry(flaky) == "ok"
    assert calls["n"] == 3

def test_retry_raises_after_exhausting_attempts():
    client = OpenAIClient.__new__(OpenAIClient)
    client.max_retries = 2
    client.backoff_base = 0.0

    def always_fail():
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError, match="boom"):
        client._retry(always_fail)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_openai_client.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
import time

from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key: str | None = None, max_retries: int = 5, backoff_base: float = 1.0):
        self._client = OpenAI(api_key=api_key) if api_key else OpenAI()
        self.max_retries = max_retries
        self.backoff_base = backoff_base

    def _retry(self, fn):
        last_exc: Exception | None = None
        for attempt in range(self.max_retries):
            try:
                return fn()
            except Exception as exc:  # noqa: BLE001 - retry any transient API error
                last_exc = exc
                if self.backoff_base:
                    time.sleep(self.backoff_base * (2 ** attempt))
        raise last_exc

    def complete(self, messages: list[dict], model: str, temperature: float = 0.0) -> str:
        resp = self._retry(
            lambda: self._client.chat.completions.create(
                model=model, messages=messages, temperature=temperature
            )
        )
        return resp.choices[0].message.content or ""

    def embed(self, texts: list[str], model: str) -> list[list[float]]:
        resp = self._retry(lambda: self._client.embeddings.create(model=model, input=texts))
        return [d.embedding for d in resp.data]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_openai_client.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/openai_client.py tests/test_openai_client.py
git commit -m "feat: add OpenAI client wrapper with exponential-backoff retry"
```

---

## Task 7: indexing/cache.py (hash + manifest + chunk persistence)

**Files:**
- Create: `src/nlp_qa_system/indexing/cache.py`
- Test: `tests/indexing/test_cache.py`

Note: `Chunk` is defined in Task 8 (`indexing/chunk.py`). To avoid a forward dependency, `cache.py` persists chunks as plain dicts and Task 8 adds the `Chunk` (de)serialization helpers there. Here we only handle hashing, the manifest, and a generic jsonl writer.

- [ ] **Step 1: Write the failing test**

Create `tests/indexing/__init__.py` (empty) and `tests/indexing/test_cache.py`:
```python
from nlp_qa_system.indexing.cache import file_sha256, load_manifest, save_manifest

def test_sha256_changes_with_content(tmp_path):
    p = tmp_path / "a.bin"
    p.write_bytes(b"hello")
    h1 = file_sha256(p)
    p.write_bytes(b"hello world")
    h2 = file_sha256(p)
    assert h1 != h2
    assert len(h1) == 64

def test_manifest_roundtrip_and_missing_default(tmp_path):
    mpath = tmp_path / "manifest.json"
    assert load_manifest(mpath) == {}
    save_manifest(mpath, {"c1.pdf": "abc"})
    assert load_manifest(mpath) == {"c1.pdf": "abc"}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/indexing/test_cache.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
import hashlib
import json
from pathlib import Path


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def load_manifest(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(path: Path, manifest: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/indexing/test_cache.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/indexing/cache.py tests/indexing
git commit -m "feat: add content-hash and manifest helpers for index cache"
```

---

## Task 8: indexing/chunk.py (Chunk type + LLM semantic chunking)

**Files:**
- Create: `src/nlp_qa_system/indexing/chunk.py`
- Test: `tests/indexing/test_chunk.py`

- [ ] **Step 1: Write the failing test**

```python
from nlp_qa_system.indexing.chunk import Chunk, semantic_chunks, save_chunks, load_chunks
from tests.conftest import FakeClient

def test_semantic_chunks_parses_json_list_and_assigns_ids():
    client = FakeClient(complete_responses=['["concept A text", "concept B text"]'])
    chunks = semantic_chunks(client, deck="c1", deck_markdown="# slides...", model="gpt-5.5")
    assert [c.text for c in chunks] == ["concept A text", "concept B text"]
    assert chunks[0].chunk_id == "c1::0"
    assert chunks[0].deck == "c1"

def test_semantic_chunks_tolerates_code_fences():
    fenced = '```json\n["only one"]\n```'
    client = FakeClient(complete_responses=[fenced])
    chunks = semantic_chunks(client, deck="c2", deck_markdown="x", model="gpt-5.5")
    assert [c.text for c in chunks] == ["only one"]

def test_chunks_jsonl_roundtrip(tmp_path):
    chunks = [Chunk("c1::0", "c1", "alpha"), Chunk("c1::1", "c1", "beta")]
    p = tmp_path / "chunks.jsonl"
    save_chunks(p, chunks)
    assert load_chunks(p) == chunks
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/indexing/test_chunk.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
import json
from dataclasses import asdict, dataclass
from pathlib import Path

CHUNK_PROMPT = """You are segmenting course-slide content into semantically coherent chunks for retrieval.

Rules:
- Split by TOPIC/CONCEPT, not by slide boundary. Merge consecutive slides on the same topic; split a slide that covers multiple topics.
- Each chunk must be self-contained and understandable on its own.
- Target 200-500 tokens per chunk, hard max ~800. Preserve original wording, formulas (LaTeX), and table content.
- Output ONLY a JSON array of strings (the chunk texts). No commentary.

Slide content:
{markdown}
"""


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    deck: str
    text: str


def _parse_json_list(raw: str) -> list[str]:
    text = raw.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[len("json"):]
        text = text.strip()
    data = json.loads(text)
    return [str(x) for x in data]


def semantic_chunks(client, deck: str, deck_markdown: str, model: str) -> list[Chunk]:
    raw = client.complete(
        [{"role": "user", "content": CHUNK_PROMPT.format(markdown=deck_markdown)}],
        model=model,
    )
    texts = _parse_json_list(raw)
    return [Chunk(chunk_id=f"{deck}::{i}", deck=deck, text=t) for i, t in enumerate(texts)]


def save_chunks(path: Path, chunks: list[Chunk]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(asdict(c), ensure_ascii=False) + "\n")


def load_chunks(path: Path) -> list[Chunk]:
    chunks: list[Chunk] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                chunks.append(Chunk(**json.loads(line)))
    return chunks
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/indexing/test_chunk.py -v`
Expected: PASS (3 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/indexing/chunk.py tests/indexing/test_chunk.py
git commit -m "feat: add Chunk type and LLM semantic chunking"
```

---

## Task 9: indexing/embed.py

**Files:**
- Create: `src/nlp_qa_system/indexing/embed.py`
- Test: `tests/indexing/test_embed.py`

- [ ] **Step 1: Write the failing test**

```python
import numpy as np
from nlp_qa_system.indexing.embed import embed_texts
from tests.conftest import FakeClient

def test_embed_texts_returns_float32_matrix():
    client = FakeClient(embeddings={"a": [1.0, 0.0], "b": [0.0, 1.0]})
    mat = embed_texts(client, ["a", "b"], model="text-embedding-3-large")
    assert mat.dtype == np.float32
    assert mat.shape == (2, 2)
    assert mat[0].tolist() == [1.0, 0.0]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/indexing/test_embed.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
import numpy as np


def embed_texts(client, texts: list[str], model: str) -> np.ndarray:
    vectors = client.embed(texts, model=model)
    return np.array(vectors, dtype="float32")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/indexing/test_embed.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/indexing/embed.py tests/indexing/test_embed.py
git commit -m "feat: add embedding helper returning float32 matrix"
```

---

## Task 10: indexing/pdf_render.py

**Files:**
- Create: `src/nlp_qa_system/indexing/pdf_render.py`
- Test: `tests/indexing/test_pdf_render.py`

- [ ] **Step 1: Write the failing test**

```python
import fitz  # pymupdf
from nlp_qa_system.indexing.pdf_render import render_pdf

def test_render_pdf_returns_one_png_per_page(tmp_path):
    doc = fitz.open()
    doc.new_page()
    doc.new_page()
    pdf_path = tmp_path / "two.pdf"
    doc.save(pdf_path)
    doc.close()

    images = render_pdf(pdf_path, dpi=72)
    assert len(images) == 2
    assert all(img[:8] == b"\x89PNG\r\n\x1a\n" for img in images)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/indexing/test_pdf_render.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
from pathlib import Path

import fitz  # pymupdf


def render_pdf(path: Path, dpi: int = 180) -> list[bytes]:
    images: list[bytes] = []
    with fitz.open(path) as doc:
        for page in doc:
            pix = page.get_pixmap(dpi=dpi)
            images.append(pix.tobytes("png"))
    return images
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/indexing/test_pdf_render.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/indexing/pdf_render.py tests/indexing/test_pdf_render.py
git commit -m "feat: add PDF page rendering to PNG via pymupdf"
```

---

## Task 11: indexing/vision_parse.py

**Files:**
- Create: `src/nlp_qa_system/indexing/vision_parse.py`
- Test: `tests/indexing/test_vision_parse.py`

- [ ] **Step 1: Write the failing test**

```python
from nlp_qa_system.indexing.vision_parse import parse_page
from tests.conftest import FakeClient

def test_parse_page_sends_image_and_returns_markdown():
    client = FakeClient(complete_responses=["# Slide title\n- bullet"])
    md = parse_page(client, image_bytes=b"\x89PNG...", model="gpt-5.5")
    assert md == "# Slide title\n- bullet"
    assert client.calls == [("complete", "gpt-5.5")]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/indexing/test_vision_parse.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
import base64

VISION_PROMPT = (
    "Transcribe this lecture slide into faithful Markdown. "
    "Keep all text and bullets verbatim. Convert tables to Markdown tables and "
    "formulas to LaTeX. For diagrams/figures/flowcharts, describe their meaning and "
    "the relationships they convey. Output only the Markdown, no commentary."
)


def parse_page(client, image_bytes: bytes, model: str) -> str:
    b64 = base64.b64encode(image_bytes).decode("ascii")
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": VISION_PROMPT},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{b64}", "detail": "high"},
                },
            ],
        }
    ]
    return client.complete(messages, model=model)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/indexing/test_vision_parse.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/indexing/vision_parse.py tests/indexing/test_vision_parse.py
git commit -m "feat: add GPT-5.5 vision page-to-markdown parsing"
```

---

## Task 12: retrieval/rerank.py

**Files:**
- Create: `src/nlp_qa_system/retrieval/rerank.py`
- Test: `tests/retrieval/test_rerank.py`

- [ ] **Step 1: Write the failing test**

```python
from nlp_qa_system.retrieval.rerank import rerank
from tests.conftest import FakeClient

def test_rerank_returns_model_order_then_fills_missing():
    # 3 candidates; model ranks [2, 0] and omits 1
    client = FakeClient(complete_responses=["[2, 0]"])
    order = rerank(client, "q", ["c0", "c1", "c2"], model="gpt-5.5", top_k=2)
    assert order[:2] == [2, 0]
    assert set(order) == {0, 1, 2}  # missing index appended

def test_rerank_falls_back_to_input_order_on_bad_json():
    client = FakeClient(complete_responses=["not json"])
    order = rerank(client, "q", ["c0", "c1"], model="gpt-5.5", top_k=2)
    assert order == [0, 1]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/retrieval/test_rerank.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
import json
import re

RERANK_PROMPT = """Rank the candidate passages by how well they help answer the question.
Return ONLY a JSON array of candidate indices, most relevant first. Include the top {top_k} at minimum.

Question: {query}

Candidates:
{candidates}
"""


def _parse_int_list(raw: str) -> list[int]:
    match = re.search(r"\[.*\]", raw, re.DOTALL)
    if not match:
        return []
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return []
    return [int(x) for x in data if isinstance(x, (int, float))]


def rerank(client, query: str, candidates: list[str], model: str, top_k: int) -> list[int]:
    listing = "\n".join(f"[{i}] {c}" for i, c in enumerate(candidates))
    raw = client.complete(
        [{"role": "user", "content": RERANK_PROMPT.format(query=query, candidates=listing, top_k=top_k)}],
        model=model,
    )
    proposed = _parse_int_list(raw)
    order = [i for i in proposed if 0 <= i < len(candidates)]
    seen = set(order)
    order.extend(i for i in range(len(candidates)) if i not in seen)
    return order
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/retrieval/test_rerank.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/retrieval/rerank.py tests/retrieval/test_rerank.py
git commit -m "feat: add GPT-5.5 listwise reranker with safe fallback"
```

---

## Task 13: qa/answer.py

**Files:**
- Create: `src/nlp_qa_system/qa/answer.py`
- Test: `tests/qa/test_answer.py`

- [ ] **Step 1: Write the failing test**

Create `tests/qa/__init__.py` (empty) and `tests/qa/test_answer.py`:
```python
from nlp_qa_system.qa.answer import generate_answer
from tests.conftest import FakeClient

def test_generate_answer_passes_context_and_returns_trimmed():
    client = FakeClient(complete_responses=["  Self-attention.  "])
    ans = generate_answer(client, "What is the core of a transformer?",
                          ["Transformers use self-attention."], model="gpt-5.5")
    assert ans == "Self-attention."
    assert client.calls == [("complete", "gpt-5.5")]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/qa/test_answer.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
ANSWER_SYSTEM = (
    "Answer the question using ONLY the provided slide excerpts. "
    "Be short and precise; do not over-explain. "
    "Answer in the same language as the question; keep technical terms in their original form. "
    "If the excerpts do not contain the answer, reply exactly '資料不足'."
)


def generate_answer(client, question: str, contexts: list[str], model: str, temperature: float = 0.0) -> str:
    joined = "\n\n---\n\n".join(contexts)
    messages = [
        {"role": "system", "content": ANSWER_SYSTEM},
        {"role": "user", "content": f"Slide excerpts:\n{joined}\n\nQuestion: {question}"},
    ]
    return client.complete(messages, model=model, temperature=temperature).strip()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/qa/test_answer.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/qa/answer.py tests/qa
git commit -m "feat: add answer generation (short, precise, grounded)"
```

---

## Task 14: indexing/build_index.py (build + load)

**Files:**
- Create: `src/nlp_qa_system/indexing/build_index.py`
- Test: `tests/indexing/test_build_index.py`

- [ ] **Step 1: Write the failing test**

```python
import fitz
import numpy as np
from nlp_qa_system.config import Config
from nlp_qa_system.indexing.build_index import build_index, load_index
from tests.conftest import FakeClient

def _make_pdf(path):
    doc = fitz.open()
    doc.new_page()
    doc.save(path)
    doc.close()

def test_build_then_load_index(tmp_path):
    slides = tmp_path / "slides"
    slides.mkdir()
    _make_pdf(slides / "c0.pdf")
    config = Config(slides_dir=slides, index_dir=tmp_path / "index")

    # 1 vision page md, then 1 chunk-list response; embeddings keyed by chunk text
    client = FakeClient(
        complete_responses=["# page md", '["alpha concept"]'],
        embeddings={"alpha concept": [1.0, 0.0]},
    )
    build_index(client, config)

    dense_idx, bm25_idx, chunks = load_index(config)
    assert [c.text for c in chunks] == ["alpha concept"]
    assert (config.index_dir / "manifest.json").exists()
    hit = dense_idx.search(np.array([1.0, 0.0], dtype="float32"), top_n=1)
    assert hit[0][0] == 0

def test_build_index_skips_unchanged_pdf_on_second_run(tmp_path):
    slides = tmp_path / "slides"
    slides.mkdir()
    _make_pdf(slides / "c0.pdf")
    config = Config(slides_dir=slides, index_dir=tmp_path / "index")

    client1 = FakeClient(complete_responses=["# page md", '["alpha"]'],
                         embeddings={"alpha": [1.0, 0.0]})
    build_index(client1, config)

    # Second run: no responses queued. If vision were called again it would IndexError.
    client2 = FakeClient(complete_responses=[], embeddings={"alpha": [1.0, 0.0]})
    build_index(client2, config)  # must hit cache and not call complete()
    assert all(kind != "complete" for kind, _ in client2.calls)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/indexing/test_build_index.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

from nlp_qa_system.config import CHUNK_MODEL, EMBED_MODEL, VISION_MODEL, Config
from nlp_qa_system.indexing.cache import file_sha256, load_manifest, save_manifest
from nlp_qa_system.indexing.chunk import Chunk, load_chunks, save_chunks, semantic_chunks
from nlp_qa_system.indexing.embed import embed_texts
from nlp_qa_system.indexing.pdf_render import render_pdf
from nlp_qa_system.indexing.vision_parse import parse_page
from nlp_qa_system.retrieval.dense import DenseIndex
from nlp_qa_system.retrieval.sparse import BM25Index


def _paths(config: Config) -> dict[str, Path]:
    d = config.index_dir
    return {
        "parsed": d / "parsed",
        "manifest": d / "manifest.json",
        "chunks": d / "chunks.jsonl",
        "embeddings": d / "embeddings.npy",
        "faiss": d / "index.faiss",
        "bm25": d / "bm25.pkl",
    }


def build_index(client, config: Config) -> None:
    p = _paths(config)
    p["parsed"].mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(p["manifest"])
    deck_markdowns: dict[str, str] = {}
    any_changed = False

    for pdf in sorted(config.slides_dir.glob("*.pdf")):
        deck = pdf.stem
        digest = file_sha256(pdf)
        md_path = p["parsed"] / f"{deck}.md"
        if manifest.get(pdf.name) == digest and md_path.exists():
            deck_markdowns[deck] = md_path.read_text(encoding="utf-8")
            continue

        any_changed = True
        images = render_pdf(pdf, config.render_dpi)
        with ThreadPoolExecutor(max_workers=config.index_concurrency) as ex:
            pages = list(ex.map(lambda img: parse_page(client, img, VISION_MODEL), images))
        markdown = "\n\n".join(pages)
        md_path.write_text(markdown, encoding="utf-8")
        deck_markdowns[deck] = markdown
        manifest[pdf.name] = digest
        save_manifest(p["manifest"], manifest)

    artifacts_exist = all(p[k].exists() for k in ("chunks", "faiss", "bm25"))
    if not any_changed and artifacts_exist:
        return

    chunks: list[Chunk] = []
    for deck, markdown in deck_markdowns.items():
        chunks.extend(semantic_chunks(client, deck, markdown, CHUNK_MODEL))
    save_chunks(p["chunks"], chunks)

    embeddings = embed_texts(client, [c.text for c in chunks], EMBED_MODEL)
    np.save(p["embeddings"], embeddings)
    DenseIndex.build(embeddings).save(p["faiss"])
    BM25Index.build([c.text for c in chunks]).save(p["bm25"])


def load_index(config: Config) -> tuple[DenseIndex, BM25Index, list[Chunk]]:
    p = _paths(config)
    return (
        DenseIndex.load(p["faiss"]),
        BM25Index.load(p["bm25"]),
        load_chunks(p["chunks"]),
    )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/indexing/test_build_index.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/indexing/build_index.py tests/indexing/test_build_index.py
git commit -m "feat: add offline index build/load with content-hash cache"
```

---

## Task 15: qa/pipeline.py (per-question + batch)

**Files:**
- Create: `src/nlp_qa_system/qa/pipeline.py`
- Test: `tests/qa/test_pipeline.py`

- [ ] **Step 1: Write the failing test**

```python
import numpy as np
from nlp_qa_system.config import Config
from nlp_qa_system.indexing.chunk import Chunk
from nlp_qa_system.retrieval.dense import DenseIndex
from nlp_qa_system.retrieval.sparse import BM25Index
from nlp_qa_system.qa.pipeline import answer_question, run_batch
from tests.conftest import FakeClient

def _fixture():
    chunks = [Chunk("c::0", "c", "transformer self-attention"),
              Chunk("c::1", "c", "bm25 ranking function")]
    emb = np.array([[1.0, 0.0], [0.0, 1.0]], dtype="float32")
    dense = DenseIndex.build(emb)
    bm25 = BM25Index.build([c.text for c in chunks])
    return chunks, dense, bm25

def test_answer_question_end_to_end():
    chunks, dense, bm25 = _fixture()
    config = Config()
    client = FakeClient(
        complete_responses=["[0, 1]", "Self-attention."],  # rerank, then answer
        embeddings={"what is a transformer": [1.0, 0.0]},
    )
    ans = answer_question(client, "what is a transformer", dense, bm25, chunks, config)
    assert ans == "Self-attention."

def test_run_batch_preserves_order():
    chunks, dense, bm25 = _fixture()
    config = Config(query_concurrency=2)
    client = FakeClient(
        complete_responses=["[0]", "A1", "[1]", "A2"],
        embeddings={"q1": [1.0, 0.0], "q2": [0.0, 1.0]},
    )
    answers = run_batch(client, ["q1", "q2"], dense, bm25, chunks, config)
    assert answers == ["A1", "A2"]
```

Note: `run_batch` must run questions sequentially-enough that the shared `FakeClient` response queue stays ordered. Implement `run_batch` to submit work but consume the queue deterministically; with `ThreadPoolExecutor.map` and `query_concurrency >= len(questions)` the FakeClient queue could interleave. To keep the test deterministic, `run_batch` processes the queue via `map` but the test uses distinct embeddings and asserts order of returned answers only — so implement `run_batch` to call `answer_question` per question and rely on `map` preserving *return* order. To avoid response-queue interleaving in the test, set `query_concurrency=1` inside this test instead.

Adjust `test_run_batch_preserves_order` to use `Config(query_concurrency=1)`.

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/qa/test_pipeline.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
from concurrent.futures import ThreadPoolExecutor

import numpy as np

from nlp_qa_system.config import ANSWER_MODEL, EMBED_MODEL, RERANK_MODEL, Config
from nlp_qa_system.qa.answer import generate_answer
from nlp_qa_system.retrieval.hybrid import rrf_fuse
from nlp_qa_system.retrieval.rerank import rerank


def answer_question(client, question, dense_idx, bm25_idx, chunks, config: Config) -> str:
    qvec = np.array(client.embed([question], EMBED_MODEL)[0], dtype="float32")
    dense_hits = dense_idx.search(qvec, config.top_n)
    sparse_hits = bm25_idx.search(question, config.top_n)
    fused = rrf_fuse([[i for i, _ in dense_hits], [i for i, _ in sparse_hits]], config.rrf_k)
    cand_idxs = [i for i, _ in fused[:config.top_n]]
    cand_texts = [chunks[i].text for i in cand_idxs]
    order = rerank(client, question, cand_texts, RERANK_MODEL, config.top_k)
    top_texts = [cand_texts[j] for j in order[:config.top_k]]
    return generate_answer(client, question, top_texts, ANSWER_MODEL, config.answer_temperature)


def run_batch(client, questions, dense_idx, bm25_idx, chunks, config: Config) -> list[str]:
    def work(q):
        return answer_question(client, q, dense_idx, bm25_idx, chunks, config)

    with ThreadPoolExecutor(max_workers=config.query_concurrency) as ex:
        return list(ex.map(work, questions))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/qa/test_pipeline.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/qa/pipeline.py tests/qa/test_pipeline.py
git commit -m "feat: add query pipeline (hybrid -> rerank -> answer) + batch"
```

---

## Task 16: __main__.py (CLI)

**Files:**
- Modify: `src/nlp_qa_system/__main__.py`
- Test: `tests/test_cli.py`

- [ ] **Step 1: Write the failing test**

```python
import sys
import numpy as np
import nlp_qa_system.__main__ as cli
from nlp_qa_system.config import Config
from nlp_qa_system.indexing.chunk import Chunk
from nlp_qa_system.retrieval.dense import DenseIndex
from nlp_qa_system.retrieval.sparse import BM25Index

def test_run_command_fills_answers(tmp_path, monkeypatch):
    inp = tmp_path / "in.csv"
    inp.write_text("q1,\n", encoding="utf-8")
    out = tmp_path / "out.csv"

    chunks = [Chunk("c::0", "c", "alpha")]
    dense = DenseIndex.build(np.array([[1.0, 0.0]], dtype="float32"))
    bm25 = BM25Index.build(["alpha"])

    monkeypatch.setattr(cli, "OpenAIClient", lambda **kw: object())
    monkeypatch.setattr(cli, "load_index", lambda config: (dense, bm25, chunks))
    monkeypatch.setattr(cli, "run_batch", lambda *a, **k: ["ANSWER"])
    monkeypatch.setattr(sys, "argv", ["prog", "run", "--input", str(inp), "--output", str(out)])

    cli.main()
    assert out.read_text(encoding="utf-8").strip() == "q1,ANSWER"

def test_index_command_invokes_build(tmp_path, monkeypatch):
    called = {"n": 0}
    monkeypatch.setattr(cli, "OpenAIClient", lambda **kw: object())
    monkeypatch.setattr(cli, "build_index", lambda client, config: called.__setitem__("n", 1))
    monkeypatch.setattr(sys, "argv", ["prog", "index"])
    cli.main()
    assert called["n"] == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_cli.py -v`
Expected: FAIL (current `__main__` only prints "Hello World!")

- [ ] **Step 3: Write minimal implementation**

Replace `src/nlp_qa_system/__main__.py` with:
```python
import argparse
from pathlib import Path

from nlp_qa_system.config import Config
from nlp_qa_system.indexing.build_index import build_index, load_index
from nlp_qa_system.io.csv_io import read_questions, write_answers
from nlp_qa_system.openai_client import OpenAIClient
from nlp_qa_system.qa.pipeline import run_batch


def main() -> None:
    parser = argparse.ArgumentParser(prog="nlp-qa-system")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("index", help="Build the offline index (untimed).")
    run_p = sub.add_parser("run", help="Answer a CSV of questions (timed).")
    run_p.add_argument("--input", required=True)
    run_p.add_argument("--output", required=True)
    args = parser.parse_args()

    config = Config()
    client = OpenAIClient(max_retries=config.max_retries)

    if args.cmd == "index":
        build_index(client, config)
    elif args.cmd == "run":
        dense_idx, bm25_idx, chunks = load_index(config)
        questions = read_questions(Path(args.input))
        answers = run_batch(client, questions, dense_idx, bm25_idx, chunks, config)
        write_answers(Path(args.output), questions, answers)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_cli.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add src/nlp_qa_system/__main__.py tests/test_cli.py
git commit -m "feat: wire CLI with index and run subcommands"
```

---

## Task 17: Full suite + integration smoke

**Files:**
- Create: `tests/test_integration.py`

- [ ] **Step 1: Write the integration test**

```python
import fitz
import numpy as np
from pathlib import Path
from nlp_qa_system.config import Config
from nlp_qa_system.indexing.build_index import build_index, load_index
from nlp_qa_system.qa.pipeline import run_batch
from tests.conftest import FakeClient

def test_index_and_answer_end_to_end(tmp_path):
    slides = tmp_path / "slides"
    slides.mkdir()
    doc = fitz.open(); doc.new_page(); doc.save(slides / "c0.pdf"); doc.close()
    config = Config(slides_dir=slides, index_dir=tmp_path / "index", query_concurrency=1)

    build_client = FakeClient(
        complete_responses=["# Transformers\nself-attention", '["transformers use self-attention"]'],
        embeddings={"transformers use self-attention": [1.0, 0.0]},
    )
    build_index(build_client, config)

    dense, bm25, chunks = load_index(config)
    query_client = FakeClient(
        complete_responses=["[0]", "Self-attention."],
        embeddings={"what do transformers use": [1.0, 0.0]},
    )
    answers = run_batch(query_client, ["what do transformers use"], dense, bm25, chunks, config)
    assert answers == ["Self-attention."]
```

- [ ] **Step 2: Run the full test suite**

Run: `uv run pytest -q`
Expected: PASS (all tasks' tests green)

- [ ] **Step 3: Commit**

```bash
git add tests/test_integration.py
git commit -m "test: add end-to-end index+answer integration test"
```

- [ ] **Step 4: Real-API smoke (manual, optional — costs money)**

Run (only when ready to validate against the real slides):
```bash
uv run python -m nlp_qa_system index
printf '什麼是 self-attention?,\n' > /tmp/q.csv
uv run python -m nlp_qa_system run --input /tmp/q.csv --output /tmp/a.csv
cat /tmp/a.csv
```
Expected: `data/index/` populated; `/tmp/a.csv` has a short, correct answer in column 2.

---

## Self-Review (completed by plan author)

**Spec coverage:**
- §3 vision-first parsing → Tasks 10, 11. Semantic chunking → Task 8. Embedding → Task 9. FAISS+BM25 → Tasks 3, 4. RRF hybrid → Task 5. GPT listwise rerank → Task 12. Answer generation → Task 13. ✅
- §5 layered content-hash cache + resumable/skip → Tasks 7, 14 (skip-unchanged test). ✅
- §6 offline `index` / timed `run`; run never builds index → Task 16 (`run` only calls `load_index` + `run_batch`). ✅
- §7 retry → Task 6; concurrency → Tasks 14 (`index_concurrency`) & 15 (`query_concurrency`); no-answer → Task 13 prompt (`資料不足`); CSV robustness → Task 2. ✅
- §8 unit tests per module + integration + gated real-API smoke → all tasks + Task 17. ✅

**Decision:** No numeric "資料不足" relevance threshold is implemented; the no-answer behavior is prompt-driven (Task 13), matching the spec note that there is no dev set to calibrate a threshold. `config.py` therefore omits a threshold field by design.

**Placeholder scan:** No TBD/TODO; every code step contains complete code. ✅

**Type consistency:** `client.complete(messages, model, temperature)` / `client.embed(texts, model)` used identically across Tasks 6, 8–15. `Chunk(chunk_id, deck, text)` consistent (Tasks 8, 14, 15, 17). `DenseIndex.search`/`BM25Index.search` return `list[tuple[int, float]]` and are consumed as such in Task 15. `rerank(...) -> list[int]` consumed with `[:top_k]` in Task 15. ✅
