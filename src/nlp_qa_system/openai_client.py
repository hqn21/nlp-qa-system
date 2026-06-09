import time

from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key: str | None = None, max_retries: int = 5, backoff_base: float = 1.0):
        self._client = OpenAI(api_key=api_key) if api_key else OpenAI()
        self.max_retries = max_retries
        self.backoff_base = backoff_base

    def _retry(self, fn):
        last_exc: Exception = RuntimeError(
            f"_retry called with max_retries={self.max_retries}; no attempt was made"
        )
        for attempt in range(self.max_retries):
            try:
                return fn()
            except Exception as exc:  # noqa: BLE001 - retry any transient API error
                last_exc = exc
                # Don't sleep after the final attempt — we're about to give up.
                if self.backoff_base and attempt < self.max_retries - 1:
                    time.sleep(self.backoff_base * (2 ** attempt))
        raise last_exc

    def complete(self, messages: list[dict], model: str, temperature: float = 0.0) -> str:
        kwargs = {
            "model": model,
            "messages": messages,
        }
        if temperature is not None and temperature > 0:
            kwargs["temperature"] = temperature
        resp = self._retry(
            lambda: self._client.chat.completions.create(**kwargs)
        )
        return resp.choices[0].message.content or ""

    def embed(self, texts: list[str], model: str) -> list[list[float]]:
        resp = self._retry(lambda: self._client.embeddings.create(model=model, input=texts))
        return [d.embedding for d in resp.data]
