"""
FastAPI router for the Financial Advisory module.

Wire this into app/main.py alongside the existing /query route:

    from financial_advisory.router import router as financial_advisory_router
    app.include_router(financial_advisory_router)

That's the only change needed in main.py. This module is intentionally
self-contained (own schemas, own eligibility + explanation logic) so it
doesn't touch the LangGraph agent, guardrails, or ingestion pipeline
built for the disease-research side of the project.

Two endpoints are exposed:
    POST /financial-advisory       - deterministic rules + template text (fast, free)
    POST /financial-advisory/rag   - deterministic rules + TF-IDF retrieval + Gemini generation
"""

from fastapi import APIRouter

from financial_advisory.eligibility import get_eligibility
from financial_advisory.explainer import generate_explanation
from financial_advisory.rag.rag_service import build_rag_report
from financial_advisory.schemas import FarmerInput, FinancialAdvisoryResponse, SchemeResult

router = APIRouter(prefix="/financial-advisory", tags=["financial-advisory"])


@router.post("", response_model=FinancialAdvisoryResponse)
def check_financial_advisory(payload: FarmerInput) -> FinancialAdvisoryResponse:
    results = get_eligibility(
        age=payload.age,
        income_annual=payload.income_annual,
        land_acres=payload.land_acres,
        dependents=payload.dependents,
    )

    scheme_results = [
        SchemeResult(
            scheme=scheme,
            eligible=eligible,
            reason=reason,
            explanation=generate_explanation(scheme, eligible, reason),
        )
        for scheme, (eligible, reason) in results.items()
    ]

    return FinancialAdvisoryResponse(results=scheme_results)


@router.post("/rag")
def check_financial_advisory_rag(payload: FarmerInput):
    return {
        "results": build_rag_report(
            age=payload.age,
            income_annual=payload.income_annual,
            land_acres=payload.land_acres,
            dependents=payload.dependents,
        )
    }
