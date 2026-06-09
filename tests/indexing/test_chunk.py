from nlp_qa_system.indexing.chunk import Chunk, semantic_chunks, save_chunks, load_chunks
from tests.conftest import FakeClient

def test_semantic_chunks_parses_json_list_and_assigns_ids():
    client = FakeClient(complete_responses=['["concept A text", "concept B text"]'])
    chunks = semantic_chunks(client, deck="c1", deck_markdown="# slides...", model="gpt-5.5")
    assert [c.text for c in chunks] == ["concept A text", "concept B text"]
    assert chunks[0].chunk_id == "c1::0"
    assert chunks[0].deck == "c1"

def test_semantic_chunks_tolerates_code_fences():
    fenced = '```json\n["only one"]\n```'
    client = FakeClient(complete_responses=[fenced])
    chunks = semantic_chunks(client, deck="c2", deck_markdown="x", model="gpt-5.5")
    assert [c.text for c in chunks] == ["only one"]

def test_chunks_jsonl_roundtrip(tmp_path):
    chunks = [Chunk("c1::0", "c1", "alpha"), Chunk("c1::1", "c1", "beta")]
    p = tmp_path / "chunks.jsonl"
    save_chunks(p, chunks)
    assert load_chunks(p) == chunks
