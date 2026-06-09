import fitz  # pymupdf
from nlp_qa_system.indexing.pdf_render import render_pdf

def test_render_pdf_returns_one_png_per_page(tmp_path):
    doc = fitz.open()
    doc.new_page()
    doc.new_page()
    pdf_path = tmp_path / "two.pdf"
    doc.save(pdf_path)
    doc.close()

    images = render_pdf(pdf_path, dpi=72)
    assert len(images) == 2
    assert all(img[:8] == b"\x89PNG\r\n\x1a\n" for img in images)
