import csv
from pathlib import Path


def read_questions(path: Path) -> list[str]:
    questions: list[str] = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            if not row:
                continue
            q = row[0].strip()
            if q:
                questions.append(q)
    return questions


def write_answers(path: Path, questions: list[str], answers: list[str]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for q, a in zip(questions, answers):
            writer.writerow([q, a])
