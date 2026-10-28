"""
Deterministic eligibility engine.

Pure rule-based logic - no LLM, no external calls - so scheme
recommendations stay accurate and auditable. This mirrors the design
principle used elsewhere in this repo's agent (grader/guardrails):
keep the parts that must be correct deterministic, and let generation
sit on top as an explanation layer, not a decision layer.
"""

from typing import Tuple


def check_kcc(age: int, land_acres: float) -> Tuple[bool, str]:
    """Kisan Credit Card: any land-owning farmer aged 18-75."""
    if land_acres > 0 and 18 <= age <= 75:
        return True, "Owns cultivable land and falls within the 18-75 age band."
    if land_acres <= 0:
        return False, "KCC requires land ownership; no land recorded."
    return False, "Age is outside the 18-75 eligibility band for KCC."


def check_pmsby(age: int) -> Tuple[bool, str]:
    """PMSBY (accident insurance): age 18-70."""
    if 18 <= age <= 70:
        return True, "Age falls within the 18-70 band for PMSBY enrollment."
    return False, "Age is outside the 18-70 eligibility band for PMSBY."


def check_apy(age: int) -> Tuple[bool, str]:
    """Atal Pension Yojana: enrollment window is age 18-40."""
    if 18 <= age <= 40:
        return True, "Age falls within the 18-40 enrollment window for APY."
    return False, "APY enrollment is only open between ages 18-40."


def check_subsidy(income_annual: float, land_acres: float, dependents: int) -> Tuple[bool, str]:
    """Small/marginal farmer subsidy: land <= 5 acres and income below threshold."""
    SMALL_FARMER_LAND_LIMIT = 5.0
    INCOME_THRESHOLD = 250000

    if land_acres <= SMALL_FARMER_LAND_LIMIT and income_annual < INCOME_THRESHOLD:
        note = "Qualifies as small/marginal farmer with income below threshold."
        if dependents >= 3:
            note += " High dependent count may raise priority in scheme allocation."
        return True, note

    reasons = []
    if land_acres > SMALL_FARMER_LAND_LIMIT:
        reasons.append(f"land ({land_acres} acres) exceeds the {SMALL_FARMER_LAND_LIMIT}-acre small-farmer limit")
    if income_annual >= INCOME_THRESHOLD:
        reasons.append(f"income (Rs.{income_annual}) is at or above the Rs.{INCOME_THRESHOLD} threshold")
    return False, "Not eligible: " + " and ".join(reasons) + "."


def get_eligibility(age: int, income_annual: float, land_acres: float, dependents: int) -> dict:
    """Runs all scheme checks. Returns {scheme: (eligible, reason)}."""
    return {
        "KCC": check_kcc(age, land_acres),
        "PMSBY": check_pmsby(age),
        "APY": check_apy(age),
        "Subsidy": check_subsidy(income_annual, land_acres, dependents),
    }
