from pathlib import Path

import faiss
import numpy as np


class DenseIndex:
    def __init__(self, index: "faiss.Index"):
        self._index = index

    @classmethod
    def build(cls, embeddings: np.ndarray) -> "DenseIndex":
        emb = np.ascontiguousarray(embeddings, dtype="float32").copy()
        faiss.normalize_L2(emb)
        index = faiss.IndexFlatIP(emb.shape[1])
        index.add(emb)
        return cls(index)

    def search(self, query: np.ndarray, top_n: int) -> list[tuple[int, float]]:
        q = np.ascontiguousarray(query, dtype="float32").reshape(1, -1).copy()
        faiss.normalize_L2(q)
        scores, ids = self._index.search(q, top_n)
        return [(int(i), float(s)) for i, s in zip(ids[0], scores[0]) if i != -1]

    def save(self, path: Path) -> None:
        faiss.write_index(self._index, str(path))

    @classmethod
    def load(cls, path: Path) -> "DenseIndex":
        return cls(faiss.read_index(str(path)))
