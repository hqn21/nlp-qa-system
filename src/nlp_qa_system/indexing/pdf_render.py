from pathlib import Path

import fitz  # pymupdf


def render_pdf(path: Path, dpi: int = 180) -> list[bytes]:
    images: list[bytes] = []
    with fitz.open(path) as doc:
        for page in doc:
            pix = page.get_pixmap(dpi=dpi)
            images.append(pix.tobytes("png"))
    return images
