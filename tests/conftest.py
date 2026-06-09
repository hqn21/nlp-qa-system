class FakeClient:
    """Stand-in for OpenAIClient. complete() pops from a queue; embed() maps text->vector."""

    def __init__(self, complete_responses=None, embeddings=None, default_dim=4):
        self._completes = list(complete_responses or [])
        self._embeddings = dict(embeddings or {})
        self._default_dim = default_dim
        self.calls = []

    def complete(self, messages, model, temperature=0.0):
        self.calls.append(("complete", model))
        if not self._completes:
            raise RuntimeError("FakeClient.complete: response queue is empty")
        return self._completes.pop(0)

    def embed(self, texts, model):
        self.calls.append(("embed", model))
        return [self._embeddings.get(t, [0.0] * self._default_dim) for t in texts]
