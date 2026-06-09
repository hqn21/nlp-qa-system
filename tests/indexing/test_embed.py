import numpy as np
from nlp_qa_system.indexing.embed import embed_texts
from tests.conftest import FakeClient

def test_embed_texts_returns_float32_matrix():
    client = FakeClient(embeddings={"a": [1.0, 0.0], "b": [0.0, 1.0]})
    mat = embed_texts(client, ["a", "b"], model="text-embedding-3-large")
    assert mat.dtype == np.float32
    assert mat.shape == (2, 2)
    assert mat[0].tolist() == [1.0, 0.0]
