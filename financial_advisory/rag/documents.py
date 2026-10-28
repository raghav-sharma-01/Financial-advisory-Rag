"""
Source documents for the Financial Advisory RAG.

These stand in for the government scheme circulars/FAQs you'd normally
ingest as PDFs (the same way DATA/*.pdf feeds the disease-advisory
RAG). Each entry is one retrievable chunk - a small, self-contained
paragraph about one aspect of one scheme, so retrieval can return
just the relevant piece instead of a whole document.

To make this closer to your main pipeline later: replace this list
with real scheme PDFs/circulars run through the same loader + chunker
you already built in app/ingestion/, and swap the retriever below for
your Qdrant collection instead of TF-IDF.
"""

DOCUMENTS = [
    {
        "id": "kcc_overview",
        "scheme": "KCC",
        "text": (
            "The Kisan Credit Card (KCC) provides farmers with timely access to short-term "
            "credit for crop production, post-harvest expenses, and farm maintenance. It "
            "offers loans at concessional interest rates, often as low as 4% per annum with "
            "timely repayment incentives."
        ),
    },
    {
        "id": "kcc_eligibility",
        "scheme": "KCC",
        "text": (
            "KCC eligibility requires the applicant to be a farmer who owns or cultivates "
            "agricultural land, typically aged between 18 and 75. Tenant farmers, "
            "sharecroppers, and oral lessees may also be eligible in many states with proper "
            "documentation."
        ),
    },
    {
        "id": "kcc_documents",
        "scheme": "KCC",
        "text": (
            "To apply for KCC, a farmer typically needs land ownership records (khatauni or "
            "similar), an Aadhaar card, a bank passbook, and passport-size photographs. "
            "Some banks also request an income certificate for higher credit limits."
        ),
    },
    {
        "id": "kcc_apply",
        "scheme": "KCC",
        "text": (
            "Farmers can apply for KCC at any nationalized or rural bank branch, or through "
            "the nearest Common Service Centre (CSC). Many banks now also accept KCC "
            "applications online through their net-banking portals."
        ),
    },
    {
        "id": "pmsby_overview",
        "scheme": "PMSBY",
        "text": (
            "Pradhan Mantri Suraksha Bima Yojana (PMSBY) is an accident insurance scheme "
            "offering coverage of up to Rs. 2 lakh for accidental death or full disability, "
            "and Rs. 1 lakh for partial disability, at a very low annual premium."
        ),
    },
    {
        "id": "pmsby_eligibility",
        "scheme": "PMSBY",
        "text": (
            "PMSBY is open to any individual aged 18 to 70 years who holds a bank account "
            "and consents to auto-debit of the annual premium. No medical examination is "
            "required to enroll."
        ),
    },
    {
        "id": "pmsby_apply",
        "scheme": "PMSBY",
        "text": (
            "Enrollment in PMSBY can be done through the policyholder's own bank, either at "
            "a branch or via net-banking/mobile banking, by submitting a simple consent form "
            "for auto-debit of the premium each year."
        ),
    },
    {
        "id": "apy_overview",
        "scheme": "APY",
        "text": (
            "Atal Pension Yojana (APY) is a government-backed pension scheme guaranteeing a "
            "fixed monthly pension between Rs. 1,000 and Rs. 5,000 after the subscriber "
            "turns 60, depending on the contribution amount chosen."
        ),
    },
    {
        "id": "apy_eligibility",
        "scheme": "APY",
        "text": (
            "APY enrollment is open only to individuals aged 18 to 40, since contributions "
            "must be made for a minimum of 20 years before the pension begins at age 60. A "
            "savings bank account or post office savings account is required."
        ),
    },
    {
        "id": "apy_apply",
        "scheme": "APY",
        "text": (
            "Subscribers can enroll in APY through their bank or post office savings "
            "account, either at a branch or through net-banking, by choosing a monthly "
            "pension amount and linking Aadhaar and a mobile number."
        ),
    },
    {
        "id": "subsidy_overview",
        "scheme": "Subsidy",
        "text": (
            "Small and marginal farmer subsidies provide financial support for seeds, "
            "fertilizers, farm equipment, and irrigation infrastructure, aimed at farmers "
            "with limited land holdings and lower annual income."
        ),
    },
    {
        "id": "subsidy_eligibility",
        "scheme": "Subsidy",
        "text": (
            "Subsidy eligibility generally applies to farmers holding up to 5 acres of land "
            "with an annual household income below a state-defined threshold. Priority is "
            "often given to households with more dependents."
        ),
    },
    {
        "id": "subsidy_documents",
        "scheme": "Subsidy",
        "text": (
            "Applying for a farmer subsidy usually requires land records, an income "
            "certificate issued by the local revenue office, and an Aadhaar card for "
            "identity verification."
        ),
    },
    {
        "id": "subsidy_apply",
        "scheme": "Subsidy",
        "text": (
            "Subsidy applications are submitted through the local agriculture department "
            "office or the state's agriculture portal, where officials verify land and "
            "income documents before approval."
        ),
    },
]
