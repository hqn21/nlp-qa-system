from nlp_qa_system.qa.answer import generate_answer
from tests.conftest import FakeClient

def test_generate_answer_passes_context_and_returns_trimmed():
    client = FakeClient(complete_responses=["  Self-attention.  "])
    ans = generate_answer(client, "What is the core of a transformer?",
                          ["Transformers use self-attention."], model="gpt-5.5")
    assert ans == "Self-attention."
    assert client.calls == [("complete", "gpt-5.5")]
