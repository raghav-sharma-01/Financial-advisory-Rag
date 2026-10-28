"""
Local scheme knowledge base.

Stands in for a proper retrieval source (this repo's Qdrant collection
uses the same "retrieve -> ground the answer" idea for the disease
corpus). If you later want real semantic retrieval here too, this dict
can be ingested into Qdrant the same way DATA/*.pdf is, using a
separate collection name (e.g. "scheme_docs") so it doesn't collide
with the disease corpus.
"""

SCHEME_KB = {
    "KCC": {
        "full_name": "Kisan Credit Card",
        "benefit": "short-term credit for seeds, fertilizer and farm expenses at low interest",
        "documents": ["land record (khatauni)", "Aadhaar card", "bank passbook"],
        "how_to_apply": "apply at your nearest bank branch or Common Service Centre (CSC)",
    },
    "PMSBY": {
        "full_name": "Pradhan Mantri Suraksha Bima Yojana",
        "benefit": "accidental death and disability insurance cover",
        "documents": ["Aadhaar card", "active bank account"],
        "how_to_apply": "enroll through your bank's net-banking or by visiting the branch",
    },
    "APY": {
        "full_name": "Atal Pension Yojana",
        "benefit": "guaranteed monthly pension after age 60",
        "documents": ["Aadhaar card", "bank account", "mobile number"],
        "how_to_apply": "enroll through your bank or post office savings account",
    },
    "Subsidy": {
        "full_name": "Small & Marginal Farmer Subsidy",
        "benefit": "financial support on seeds, equipment or irrigation costs",
        "documents": ["land record", "income certificate", "Aadhaar card"],
        "how_to_apply": "apply through your local agriculture department office",
    },
}


def retrieve(scheme_name: str):
    return SCHEME_KB.get(scheme_name)
