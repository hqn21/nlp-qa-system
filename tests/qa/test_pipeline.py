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
    config = Config(query_concurrency=1)
    client = FakeClient(
        complete_responses=["[0]", "A1", "[1]", "A2"],
        embeddings={"q1": [1.0, 0.0], "q2": [0.0, 1.0]},
    )
    answers = run_batch(client, ["q1", "q2"], dense, bm25, chunks, config)
    assert answers == ["A1", "A2"]
