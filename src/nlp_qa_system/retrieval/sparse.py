import pickle
from pathlib import Path

import jieba
from rank_bm25 import BM25Plus


def tokenize(text: str) -> list[str]:
    return [t for t in jieba.lcut(text.lower()) if t.strip()]


class BM25Index:
    def __init__(self, bm25: BM25Plus):
        self._bm25 = bm25

    @classmethod
    def build(cls, texts: list[str]) -> "BM25Index":
        tokenized = [tokenize(t) for t in texts]
        return cls(BM25Plus(tokenized))

    def search(self, query: str, top_n: int) -> list[tuple[int, float]]:
        scores = self._bm25.get_scores(tokenize(query))
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return [(i, float(scores[i])) for i in ranked[:top_n]]

    def save(self, path: Path) -> None:
        with open(path, "wb") as f:
            pickle.dump(self._bm25, f)

    @classmethod
    def load(cls, path: Path) -> "BM25Index":
        with open(path, "rb") as f:
            return cls(pickle.load(f))
