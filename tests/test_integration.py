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
