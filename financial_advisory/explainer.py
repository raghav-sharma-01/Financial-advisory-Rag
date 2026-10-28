"""
Explanation layer: retrieval + template fill. No LLM call.

If you later want to route this through the LLM gateway already built
in app/llm/router.py (Groq -> Gemini fallback chain), that would slot
in right here - generate_explanation() is the only function that
would need to change, everything upstream (eligibility.py) stays
untouched.
"""

from financial_advisory.knowledge_base import retrieve


def generate_explanation(scheme_name: str, eligible: bool, reason: str) -> str:
    doc = retrieve(scheme_name)
    if doc is None:
        return f"{scheme_name}: no information found in knowledge base."

    if not eligible:
        return f"{doc['full_name']} ({scheme_name}): {reason}"

    docs_list = ", ".join(doc["documents"])
    return (
        f"{doc['full_name']} ({scheme_name}): You are ELIGIBLE. {reason} "
        f"Benefit: {doc['benefit']}. "
        f"Documents needed: {docs_list}. "
        f"How to apply: {doc['how_to_apply']}."
    )
