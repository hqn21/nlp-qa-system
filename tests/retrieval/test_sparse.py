from nlp_qa_system.retrieval.sparse import tokenize, BM25Index

def test_tokenize_mixed_language_lowercases():
    toks = tokenize("Transformer 是一種 NLP 模型")
    assert "transformer" in toks
    assert "nlp" in toks

def test_bm25_ranks_relevant_doc_first():
    docs = [
        "BM25 是一種詞頻排序演算法",
        "transformer 使用 self-attention",
        "cipher decryption 與密碼學",
    ]
    idx = BM25Index.build(docs)
    hits = idx.search("self-attention transformer", top_n=3)
    assert hits[0][0] == 1

def test_bm25_save_load_roundtrip(tmp_path):
    idx = BM25Index.build(["alpha beta", "gamma delta"])
    p = tmp_path / "bm25.pkl"
    idx.save(p)
    loaded = BM25Index.load(p)
    assert loaded.search("gamma", top_n=1)[0][0] == 1
