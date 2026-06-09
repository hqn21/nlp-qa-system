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

def test_rerank_dedups_repeated_indices_into_full_permutation():
    # Model repeats index 2; result must stay a permutation of 0..2 (no dup, no drop).
    client = FakeClient(complete_responses=["[2, 0, 2]"])
    order = rerank(client, "q", ["c0", "c1", "c2"], model="gpt-5.5", top_k=2)
    assert order == [2, 0, 1]
    assert len(order) == 3

def test_rerank_ignores_out_of_range_indices():
    # Model proposes index 5 which doesn't exist (only 2 candidates).
    client = FakeClient(complete_responses=["[5, 1, 0]"])
    order = rerank(client, "q", ["c0", "c1"], model="gpt-5.5", top_k=2)
    assert order == [1, 0]

def test_rerank_extracts_first_array_amid_prose():
    # Non-greedy regex grabs the first array even with a trailing one.
    client = FakeClient(complete_responses=["best: [1, 0] (ignore [9, 9])"])
    order = rerank(client, "q", ["c0", "c1"], model="gpt-5.5", top_k=2)
    assert order == [1, 0]
