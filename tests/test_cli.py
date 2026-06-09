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

def test_run_without_index_raises_friendly_error(tmp_path, monkeypatch):
    import pytest
    inp = tmp_path / "in.csv"
    inp.write_text("q1,\n", encoding="utf-8")
    out = tmp_path / "out.csv"
    # Point index_dir at an empty dir via a Config whose index_dir doesn't exist.
    monkeypatch.setattr(cli, "OpenAIClient", lambda **kw: object())
    monkeypatch.setattr(cli, "Config", lambda: __import__("nlp_qa_system.config", fromlist=["Config"]).Config(index_dir=tmp_path / "missing"))
    monkeypatch.setattr(sys, "argv", ["prog", "run", "--input", str(inp), "--output", str(out)])
    with pytest.raises(SystemExit) as exc:
        cli.main()
    assert "index" in str(exc.value).lower()

def test_index_command_invokes_build(tmp_path, monkeypatch):
    called = {"n": 0}
    monkeypatch.setattr(cli, "OpenAIClient", lambda **kw: object())
    monkeypatch.setattr(cli, "build_index", lambda client, config: called.__setitem__("n", 1))
    monkeypatch.setattr(sys, "argv", ["prog", "index"])
    cli.main()
    assert called["n"] == 1
