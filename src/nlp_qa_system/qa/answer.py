ANSWER_SYSTEM = (
    "Answer the question using ONLY the provided slide excerpts. "
    "Be short and precise; do not over-explain. "
    "Answer in the same language as the question; keep technical terms in their original form. "
    "Reply in plain text only. Do NOT use any Markdown formatting: "
    "no headings, bold, italics, bullet or numbered lists, tables, code fences, or backticks. "
    "Do NOT use LaTeX or math markup; write formulas and symbols in plain Unicode text "
    "(e.g. α, ≤, x², not \\alpha, \\leq, x^2 or $...$). "
    "If the excerpts do not contain the answer, reply exactly '資料不足'."
)


def generate_answer(client, question: str, contexts: list[str], model: str, temperature: float = 0.0) -> str:
    joined = "\n\n---\n\n".join(contexts)
    messages = [
        {"role": "system", "content": ANSWER_SYSTEM},
        {"role": "user", "content": f"Slide excerpts:\n{joined}\n\nQuestion: {question}"},
    ]
    return client.complete(messages, model=model, temperature=temperature).strip()
