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
