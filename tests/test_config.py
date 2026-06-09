from pathlib import Path
from nlp_qa_system.config import Config, EMBED_MODEL, ANSWER_MODEL

def test_config_defaults():
    c = Config()
    assert c.top_n == 20
    assert c.top_k == 6
    assert c.rrf_k == 60
    assert c.query_concurrency == 8
    assert c.index_dir == Path("data/index")
    assert EMBED_MODEL == "text-embedding-3-large"
    assert ANSWER_MODEL == "gpt-5.5"
