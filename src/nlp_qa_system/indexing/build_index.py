from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

from nlp_qa_system.config import CHUNK_MODEL, EMBED_MODEL, VISION_MODEL, Config
from nlp_qa_system.indexing.cache import file_sha256, load_manifest, save_manifest
from nlp_qa_system.indexing.chunk import Chunk, load_chunks, save_chunks, semantic_chunks
from nlp_qa_system.indexing.embed import embed_texts
from nlp_qa_system.indexing.pdf_render import render_pdf
from nlp_qa_system.indexing.vision_parse import parse_page
from nlp_qa_system.retrieval.dense import DenseIndex
from nlp_qa_system.retrieval.sparse import BM25Index


def _paths(config: Config) -> dict[str, Path]:
    d = config.index_dir
    return {
        "parsed": d / "parsed",
        "manifest": d / "manifest.json",
        "chunks": d / "chunks.jsonl",
        "embeddings": d / "embeddings.npy",
        "faiss": d / "index.faiss",
        "bm25": d / "bm25.pkl",
    }


def build_index(client, config: Config) -> None:
    p = _paths(config)
    p["parsed"].mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(p["manifest"])
    deck_markdowns: dict[str, str] = {}
    any_changed = False

    for pdf in sorted(config.slides_dir.glob("*.pdf")):
        deck = pdf.stem
        digest = file_sha256(pdf)
        md_path = p["parsed"] / f"{deck}.md"
        if manifest.get(pdf.name) == digest and md_path.exists():
            deck_markdowns[deck] = md_path.read_text(encoding="utf-8")
            continue

        any_changed = True
        images = render_pdf(pdf, config.render_dpi)
        with ThreadPoolExecutor(max_workers=config.index_concurrency) as ex:
            pages = list(ex.map(lambda img: parse_page(client, img, VISION_MODEL), images))
        markdown = "\n\n".join(pages)
        md_path.write_text(markdown, encoding="utf-8")
        deck_markdowns[deck] = markdown
        manifest[pdf.name] = digest
        save_manifest(p["manifest"], manifest)

    artifacts_exist = all(p[k].exists() for k in ("chunks", "faiss", "bm25"))
    if not any_changed and artifacts_exist:
        return

    chunks: list[Chunk] = []
    for deck, markdown in deck_markdowns.items():
        chunks.extend(semantic_chunks(client, deck, markdown, CHUNK_MODEL))
    save_chunks(p["chunks"], chunks)

    embeddings = embed_texts(client, [c.text for c in chunks], EMBED_MODEL)
    np.save(p["embeddings"], embeddings)
    DenseIndex.build(embeddings).save(p["faiss"])
    BM25Index.build([c.text for c in chunks]).save(p["bm25"])


def load_index(config: Config) -> tuple[DenseIndex, BM25Index, list[Chunk]]:
    p = _paths(config)
    return (
        DenseIndex.load(p["faiss"]),
        BM25Index.load(p["bm25"]),
        load_chunks(p["chunks"]),
    )
