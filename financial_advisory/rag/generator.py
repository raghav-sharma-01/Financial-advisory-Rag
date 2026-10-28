"""
Generation layer: calls Gemini with retrieved context to produce the
final farmer-facing explanation. This is the "G" in RAG - an actual
LLM call, grounded in the chunks retriever.py returned, not a
template fill.

Requires GEMINI_API_KEY to be set (same variable name your main
project's .env already uses, per your README).
"""

import os
import requests

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = os.environ.get("GEMINI_CHAT_MODEL", "gemini-1.5-flash")
GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
)


def generate_answer(question: str, context_chunks: list[dict]) -> str:
    """
    question: the farmer's situation/query, e.g. "Am I eligible for KCC?"
    context_chunks: output of retriever.retrieve() - list of {scheme, text, ...}
    """
    if not GEMINI_API_KEY:
        return (
            "[Gemini not configured] Set GEMINI_API_KEY in your environment to enable "
            "generated explanations. Retrieved context:\n"
            + "\n".join(f"- {c['text']}" for c in context_chunks)
        )

    context_text = "\n".join(f"- {c['text']}" for c in context_chunks)

    prompt = (
        "You are a financial advisory assistant helping a rural farmer in India. "
        "Answer ONLY using the context below. Keep the answer short, plain-language, "
        "and practical - suitable to be read aloud to someone with no financial "
        "background. Do not invent facts not present in the context.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Farmer's question: {question}\n\n"
        "Answer:"
    )

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        response = requests.post(
            GEMINI_URL,
            params={"key": GEMINI_API_KEY},
            json=payload,
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except requests.exceptions.RequestException as exc:
        return f"[Gemini call failed: {exc}]"
    except (KeyError, IndexError):
        return "[Gemini returned an unexpected response format]"
