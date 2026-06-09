import json
import re

RERANK_PROMPT = """Rank the candidate passages by how well they help answer the question.
Return ONLY a JSON array of candidate indices, most relevant first. Include the top {top_k} at minimum.

Question: {query}

Candidates:
{candidates}
"""


def _parse_int_list(raw: str) -> list[int]:
    match = re.search(r"\[.*\]", raw, re.DOTALL)
    if not match:
        return []
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return []
    return [int(x) for x in data if isinstance(x, (int, float))]


def rerank(client, query: str, candidates: list[str], model: str, top_k: int) -> list[int]:
    listing = "\n".join(f"[{i}] {c}" for i, c in enumerate(candidates))
    raw = client.complete(
        [{"role": "user", "content": RERANK_PROMPT.format(query=query, candidates=listing, top_k=top_k)}],
        model=model,
    )
    proposed = _parse_int_list(raw)
    order = [i for i in proposed if 0 <= i < len(candidates)]
    seen = set(order)
    order.extend(i for i in range(len(candidates)) if i not in seen)
    return order
