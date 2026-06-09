import base64

VISION_PROMPT = (
    "Transcribe this lecture slide into faithful Markdown. "
    "Keep all text and bullets verbatim. Convert tables to Markdown tables and "
    "formulas to LaTeX. For diagrams/figures/flowcharts, describe their meaning and "
    "the relationships they convey. Output only the Markdown, no commentary."
)


def parse_page(client, image_bytes: bytes, model: str) -> str:
    b64 = base64.b64encode(image_bytes).decode("ascii")
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": VISION_PROMPT},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{b64}", "detail": "high"},
                },
            ],
        }
    ]
    return client.complete(messages, model=model)
