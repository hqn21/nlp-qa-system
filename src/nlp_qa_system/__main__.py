import argparse
from pathlib import Path

from dotenv import load_dotenv

from nlp_qa_system.config import Config
from nlp_qa_system.indexing.build_index import build_index, load_index
from nlp_qa_system.io.csv_io import read_questions, write_answers
from nlp_qa_system.openai_client import OpenAIClient
from nlp_qa_system.qa.pipeline import run_batch


def main() -> None:
    # Load OPENAI_API_KEY (and any other vars) from a local .env if present.
    load_dotenv()

    parser = argparse.ArgumentParser(prog="nlp-qa-system")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("index", help="Build the offline index (untimed).")
    run_p = sub.add_parser("run", help="Answer a CSV of questions (timed).")
    run_p.add_argument("--input", required=True)
    run_p.add_argument("--output", required=True)
    args = parser.parse_args()

    config = Config()
    client = OpenAIClient(max_retries=config.max_retries)

    if args.cmd == "index":
        build_index(client, config)
    elif args.cmd == "run":
        try:
            dense_idx, bm25_idx, chunks = load_index(config)
        except (FileNotFoundError, RuntimeError):
            raise SystemExit(
                f"No index found at {config.index_dir}. Run `nlp-qa-system index` first."
            )
        questions = read_questions(Path(args.input))
        answers = run_batch(client, questions, dense_idx, bm25_idx, chunks, config)
        write_answers(Path(args.output), questions, answers)


if __name__ == "__main__":
    main()
