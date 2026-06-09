# NLP QA System

A retrieval-augmented question-answering system for Natural Language Processing course materials, developed as a final project.

The project converts PDF lecture slides into structured Markdown, divides the content into semantic chunks, builds dense and sparse retrieval indexes, reranks the retrieved passages, and generates concise answers grounded only in the course materials.

## Features

- Vision-based PDF slide transcription into Markdown
- Semantic chunking across slide boundaries
- Dense retrieval with OpenAI embeddings and FAISS
- Sparse retrieval with Jieba tokenization and BM25Plus
- Reciprocal Rank Fusion for hybrid retrieval
- LLM-based passage reranking
- Grounded answer generation in the same language as the question
- Parallel batch processing for CSV question files
- Incremental PDF parsing with SHA-256-based caching

## System Pipeline

```text
PDF lecture slides
        |
        v
Render each page as a PNG image
        |
        v
Vision model transcription to Markdown
        |
        v
LLM-based semantic chunking
        |
        +-------------------------------+
        |                               |
        v                               v
OpenAI embeddings                  Jieba tokenization
        |                               |
        v                               v
FAISS dense index                  BM25Plus sparse index
        |                               |
        +---------------+---------------+
                        |
                        v
             Reciprocal Rank Fusion
                        |
                        v
                  LLM reranking
                        |
                        v
              Grounded answer generation
```

For each question, the system retrieves candidates from both indexes, fuses the rankings, reranks the best candidates, and answers using only the selected slide excerpts. When the retrieved material does not contain enough information, the system returns a response indicating that the available information is insufficient.

## Requirements

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)
- An OpenAI API key with access to the models configured in `src/nlp_qa_system/config.py`
- Internet access while building the index and answering questions

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/hqn21/nlp-qa-system.git
cd nlp-qa-system
```

Install the project and its dependencies:

```bash
uv sync
```

Create a local environment file:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the placeholder with your API key:

```dotenv
OPENAI_API_KEY=your_openai_api_key
```

Do not commit the `.env` file or expose the API key publicly.

## Quick Start

Run all commands from the repository root because the default slide and index paths are relative to that directory.

### 1. Prepare the lecture slides

Place PDF files in:

```text
docs/slides/
```

The repository already includes the NLP course slide decks used by this project. Any additional course material must also be provided as a PDF.

### 2. Build the index

```bash
uv run nlp-qa-system index
```

Equivalent module command:

```bash
uv run python -m nlp_qa_system index
```

The indexing command performs the following operations:

1. Renders every PDF page as a PNG image.
2. Uses the configured vision model to transcribe each page into Markdown.
3. Uses the configured chunking model to create semantically coherent chunks.
4. Generates embeddings for all chunks.
5. Builds a FAISS dense index.
6. Builds a BM25Plus sparse index.
7. Saves the generated artifacts under `data/index/`.

The initial indexing run can make many API requests because each PDF page is processed independently. Parsed results are cached, so unchanged PDFs are not transcribed again on later runs.

### 3. Answer a CSV file

The repository includes an example question file at `data/eval/question.csv`.

```bash
uv run nlp-qa-system run \
  --input data/eval/question.csv \
  --output data/eval/answer.csv
```

On Windows PowerShell, the same command can be written on one line:

```powershell
uv run nlp-qa-system run --input data/eval/question.csv --output data/eval/answer.csv
```

The output CSV contains each original question and its generated answer.

## Command-Line Interface

### Build or update the index

```text
nlp-qa-system index
```

This command reads all `*.pdf` files in `docs/slides/` and writes the index artifacts to `data/index/`.

### Run batch question answering

```text
nlp-qa-system run --input INPUT_CSV --output OUTPUT_CSV
```

Arguments:

| Argument | Required | Description |
| --- | --- | --- |
| `--input` | Yes | Path to the CSV file containing questions. |
| `--output` | Yes | Path where the generated answer CSV will be written. |

The `run` command requires an existing index. If the index is missing, run `nlp-qa-system index` first.

## CSV Format

### Input

The input file must not contain a header row. The first column of every non-empty row is treated as the question. Additional columns are ignored, so the second column may be left blank when required by an evaluation format.

Example:

```csv
"What is the difference between CBOW and Skip-gram?",
"How does self-attention work in a Transformer?",
"What is BM25?",
```

The reader accepts UTF-8 files both with and without a byte order mark.

### Output

The output file has no header and contains two columns:

1. Original question
2. Generated answer

Example:

```csv
"What is BM25?","BM25 is a probabilistic sparse-retrieval ranking function based on term frequency and inverse document frequency."
```

The output is written as UTF-8 with a byte order mark for compatibility with applications such as Microsoft Excel.

## Index Artifacts

The indexing process creates the following files under `data/index/`:

| Path | Purpose |
| --- | --- |
| `parsed/` | Markdown transcriptions generated from individual PDF decks. |
| `manifest.json` | SHA-256 hashes used to detect modified PDFs. |
| `chunks.jsonl` | Semantic chunks with their deck names and chunk identifiers. |
| `embeddings.npy` | Dense embedding matrix for the generated chunks. |
| `index.faiss` | FAISS dense-retrieval index. |
| `bm25.pkl` | Serialized BM25Plus sparse-retrieval index. |
| `index.ready` | Manifest snapshot indicating that all index artifacts were built successfully. |

### Rebuilding the index

After adding or modifying a PDF, run the indexing command again:

```bash
uv run nlp-qa-system index
```

To force a completely clean rebuild on macOS or Linux:

```bash
rm -rf data/index
uv run nlp-qa-system index
```

On Windows PowerShell:

```powershell
Remove-Item -Recurse -Force data/index
uv run nlp-qa-system index
```

A clean rebuild is useful after removing slide files, changing indexing models, or changing index-related configuration values.

## Default Configuration

The main configuration is defined in `src/nlp_qa_system/config.py`.

### Models

| Stage | Default model |
| --- | --- |
| Slide transcription | `gpt-5.5` |
| Semantic chunking | `gpt-5.5` |
| Passage reranking | `gpt-5.5` |
| Answer generation | `gpt-5.5` |
| Embeddings | `text-embedding-3-large` |

If the configured models are unavailable to your API account, update the corresponding constants in `config.py` before building the index.

### Retrieval and concurrency settings

| Setting | Default | Description |
| --- | ---: | --- |
| `render_dpi` | `180` | Resolution used when rendering PDF pages. |
| `top_n` | `20` | Number of candidates retrieved from each retrieval stage. |
| `top_k` | `6` | Number of reranked passages supplied to answer generation. |
| `rrf_k` | `60` | Reciprocal Rank Fusion constant. |
| `query_concurrency` | `8` | Maximum number of questions processed concurrently. |
| `index_concurrency` | `8` | Maximum number of slide pages transcribed concurrently. |
| `max_retries` | `5` | Maximum number of attempts for an OpenAI API call. |
| `answer_temperature` | `0.0` | Answer-generation temperature. |

Reduce the concurrency values when encountering API rate limits or local resource constraints.

## API Request Behavior

During indexing:

- Each uncached PDF page produces one vision-model request.
- Each PDF deck produces one semantic-chunking request when the index is rebuilt.
- The generated chunks are sent to the embedding API to build the dense index.

For each question:

- One embedding request is used for dense retrieval.
- One chat-completion request is used for reranking.
- One chat-completion request is used for answer generation.

Questions are processed concurrently according to `query_concurrency`. API usage may therefore occur in bursts, and normal OpenAI API charges apply.

## Project Structure

```text
nlp-qa-system/
├── data/
│   ├── eval/                  # Example question and answer CSV files
│   └── index/                 # Generated retrieval artifacts
├── docs/
│   └── slides/                # Source PDF lecture slides
├── src/
│   └── nlp_qa_system/
│       ├── indexing/          # PDF rendering, parsing, chunking, and indexing
│       ├── io/                # CSV input and output
│       ├── qa/                # Question-answering pipeline
│       ├── retrieval/         # Dense, sparse, hybrid, and reranking logic
│       ├── __main__.py        # CLI entry point
│       ├── config.py          # Models, paths, and runtime settings
│       └── openai_client.py   # OpenAI client with retry handling
├── tests/                     # Unit and integration tests
├── .env.example              # Environment variable template
├── pyproject.toml            # Project metadata and dependencies
└── uv.lock                   # Locked dependency versions
```

## Running the Tests

Install the development dependency group and run the test suite:

```bash
uv sync --group dev
uv run pytest
```

Run a specific test file:

```bash
uv run pytest tests/test_cli.py
```

Run tests with verbose output:

```bash
uv run pytest -v
```

The test suite uses local test doubles and does not require live OpenAI API calls.

## Troubleshooting

### `No index found at data/index`

Build the index before running question answering:

```bash
uv run nlp-qa-system index
```

### Authentication or missing API key error

Confirm that `.env` exists in the repository root and contains a valid value:

```dotenv
OPENAI_API_KEY=your_openai_api_key
```

### Model access error

The API account must have access to every model configured in `src/nlp_qa_system/config.py`. Change the relevant model constants when necessary, then perform a clean index rebuild if the vision, chunking, or embedding model changed.

### Rate-limit errors

Lower `index_concurrency` or `query_concurrency` in `config.py`. The client retries failed API calls with exponential backoff, but sustained rate limits may still require lower concurrency.

### The output repeatedly indicates that the available information is insufficient

Check that:

- The relevant PDFs are present in `docs/slides/`.
- The index was rebuilt after the PDFs were added or modified.
- The generated Markdown files in `data/index/parsed/` contain the expected content.
- The question can be answered from the indexed course materials.

### The CSV displays garbled text

The generated output uses UTF-8 with a byte order mark. When importing the file manually, select UTF-8 instead of a legacy encoding.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
