from pydantic import BaseModel, Field


class FarmerInput(BaseModel):
    age: int = Field(..., ge=0, le=120)
    income_annual: float = Field(..., ge=0)
    land_acres: float = Field(..., ge=0)
    dependents: int = Field(..., ge=0)


class SchemeResult(BaseModel):
    scheme: str
    eligible: bool
    reason: str
    explanation: str


class FinancialAdvisoryResponse(BaseModel):
    results: list[SchemeResult]
