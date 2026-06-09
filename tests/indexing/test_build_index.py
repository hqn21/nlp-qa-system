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

    # Second run: no responses queued. If vision were called again it would error.
    client2 = FakeClient(complete_responses=[], embeddings={"alpha": [1.0, 0.0]})
    build_index(client2, config)  # must hit cache and not call complete()
    assert all(kind != "complete" for kind, _ in client2.calls)
