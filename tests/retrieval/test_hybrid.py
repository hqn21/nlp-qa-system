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
