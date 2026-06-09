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
