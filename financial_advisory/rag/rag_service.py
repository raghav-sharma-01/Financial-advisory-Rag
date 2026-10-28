"""
Orchestrates the full RAG flow for one farmer:

    1. Run deterministic eligibility (eligibility.py) - unchanged,
       still the trustworthy decision layer.
    2. For each eligible scheme, build a query and retrieve relevant
       chunks (retriever.py - TF-IDF).
    3. Generate a plain-language explanation grounded in those chunks
       (generator.py - Gemini).

Ineligible schemes skip retrieval/generation entirely (no benefit to
generating an explanation for something the farmer can't get, and it
saves API calls).
"""

from financial_advisory.eligibility import get_eligibility
from financial_advisory.rag.generator import generate_answer
from financial_advisory.rag.retriever import retrieve


def build_rag_report(age: int, income_annual: float, land_acres: float, dependents: int) -> list[dict]:
    results = get_eligibility(age, income_annual, land_acres, dependents)
    report = []

    for scheme, (eligible, reason) in results.items():
        if not eligible:
            report.append(
                {
                    "scheme": scheme,
                    "eligible": False,
                    "reason": reason,
                    "explanation": reason,  # no need to retrieve/generate for ineligible
                    "sources": [],
                }
            )
            continue

        query = f"How does {scheme} work and how do I apply? Context: {reason}"
        chunks = retrieve(query, top_k=3, scheme_filter=scheme)
        explanation = generate_answer(query, chunks)

        report.append(
            {
                "scheme": scheme,
                "eligible": True,
                "reason": reason,
                "explanation": explanation,
                "sources": [c["id"] for c in chunks],
            }
        )

    return report
