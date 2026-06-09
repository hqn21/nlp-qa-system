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
