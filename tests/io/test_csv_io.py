from pathlib import Path
from nlp_qa_system.io.csv_io import read_questions, write_answers

def test_read_questions_two_columns_no_header(tmp_path: Path):
    p = tmp_path / "in.csv"
    p.write_text("什麼是 transformer?,\nWhat is BM25?,\n", encoding="utf-8")
    assert read_questions(p) == ["什麼是 transformer?", "What is BM25?"]

def test_read_skips_blank_rows(tmp_path: Path):
    p = tmp_path / "in.csv"
    p.write_text("Q1,\n\n,\nQ2,\n", encoding="utf-8")
    assert read_questions(p) == ["Q1", "Q2"]

def test_read_handles_bom(tmp_path: Path):
    p = tmp_path / "in.csv"
    p.write_text("Q1,\n", encoding="utf-8-sig")
    assert read_questions(p) == ["Q1"]

def test_write_answers_roundtrip_preserves_order_and_quoting(tmp_path: Path):
    out = tmp_path / "out.csv"
    write_answers(out, ["Q1", 'Has, comma'], ["A1", 'multi\nline'])
    import csv
    with open(out, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert rows == [["Q1", "A1"], ["Has, comma", "multi\nline"]]
