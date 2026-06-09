from concurrent.futures import ThreadPoolExecutor

import numpy as np

from nlp_qa_system.config import ANSWER_MODEL, EMBED_MODEL, RERANK_MODEL, Config
from nlp_qa_system.qa.answer import generate_answer
from nlp_qa_system.retrieval.hybrid import rrf_fuse
from nlp_qa_system.retrieval.rerank import rerank


def answer_question(client, question, dense_idx, bm25_idx, chunks, config: Config) -> str:
    qvec = np.array(client.embed([question], EMBED_MODEL)[0], dtype="float32")
    dense_hits = dense_idx.search(qvec, config.top_n)
    sparse_hits = bm25_idx.search(question, config.top_n)
    fused = rrf_fuse([[i for i, _ in dense_hits], [i for i, _ in sparse_hits]], config.rrf_k)
    cand_idxs = [i for i, _ in fused[:config.top_n]]
    cand_texts = [chunks[i].text for i in cand_idxs]
    order = rerank(client, question, cand_texts, RERANK_MODEL, config.top_k)
    top_texts = [cand_texts[j] for j in order[:config.top_k]]
    return generate_answer(client, question, top_texts, ANSWER_MODEL, config.answer_temperature)


def run_batch(client, questions, dense_idx, bm25_idx, chunks, config: Config) -> list[str]:
    def work(q):
        return answer_question(client, q, dense_idx, bm25_idx, chunks, config)

    with ThreadPoolExecutor(max_workers=config.query_concurrency) as ex:
        return list(ex.map(work, questions))
