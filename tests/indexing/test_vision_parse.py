from nlp_qa_system.indexing.vision_parse import parse_page
from tests.conftest import FakeClient


def test_parse_page_sends_image_and_returns_markdown():
    client = FakeClient(complete_responses=["# Slide title\n- bullet"])
    md = parse_page(client, image_bytes=b"\x89PNG...", model="gpt-5.5")
    assert md == "# Slide title\n- bullet"
    assert client.calls == [("complete", "gpt-5.5")]
