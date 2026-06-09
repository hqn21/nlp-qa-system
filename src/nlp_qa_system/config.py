from dataclasses import dataclass
from pathlib import Path

VISION_MODEL = "gpt-5.5"
CHUNK_MODEL = "gpt-5.5"
RERANK_MODEL = "gpt-5.5"
ANSWER_MODEL = "gpt-5.5"
EMBED_MODEL = "text-embedding-3-large"


@dataclass(frozen=True)
class Config:
    slides_dir: Path = Path("docs/slides")
    index_dir: Path = Path("data/index")
    render_dpi: int = 180
    top_n: int = 20
    top_k: int = 6
    rrf_k: int = 60
    query_concurrency: int = 8
    index_concurrency: int = 8
    max_retries: int = 5
    answer_temperature: float = 0.0
