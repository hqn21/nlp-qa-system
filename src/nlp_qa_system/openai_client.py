import time

from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key: str | None = None, max_retries: int = 5, backoff_base: float = 1.0):
        self._client = OpenAI(api_key=api_key) if api_key else OpenAI()
        self.max_retries = max_retries
        self.backoff_base = backoff_base

    def _retry(self, fn):
        last_exc: Exception | None = None
        for attempt in range(self.max_retries):
            try:
                return fn()
            except Exception as exc:  # noqa: BLE001 - retry any transient API error
                last_exc = exc
                if self.backoff_base:
                    time.sleep(self.backoff_base * (2 ** attempt))
        raise last_exc

    def complete(self, messages: list[dict], model: str, temperature: float = 0.0) -> str:
        resp = self._retry(
            lambda: self._client.chat.completions.create(
                model=model, messages=messages, temperature=temperature
            )
        )
        return resp.choices[0].message.content or ""

    def embed(self, texts: list[str], model: str) -> list[list[float]]:
        resp = self._retry(lambda: self._client.embeddings.create(model=model, input=texts))
        return [d.embedding for d in resp.data]
