import numpy as np


def embed_texts(client, texts: list[str], model: str) -> np.ndarray:
    vectors = client.embed(texts, model=model)
    return np.array(vectors, dtype="float32")
