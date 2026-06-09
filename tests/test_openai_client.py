import pytest
from nlp_qa_system.openai_client import OpenAIClient

def test_retry_succeeds_after_transient_failures():
    client = OpenAIClient.__new__(OpenAIClient)  # bypass __init__/network
    client.max_retries = 5
    client.backoff_base = 0.0
    calls = {"n": 0}

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise RuntimeError("rate limited")
        return "ok"

    assert client._retry(flaky) == "ok"
    assert calls["n"] == 3

def test_retry_raises_after_exhausting_attempts():
    client = OpenAIClient.__new__(OpenAIClient)
    client.max_retries = 2
    client.backoff_base = 0.0

    def always_fail():
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError, match="boom"):
        client._retry(always_fail)
