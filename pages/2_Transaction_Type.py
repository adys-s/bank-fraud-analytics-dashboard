# ==========================================================
# TRANSACTION TYPE ANALYSIS
# ==========================================================

# ==========================
# Import libraries
# ==========================

from utils import (
    page_title,
    section_title,
    display_image,
    display_analysis
)

# ==========================================================
# Page title
# ==========================================================

page_title(
    "Transaction Type Analysis",
    "This section analyses the relationship between transaction types and fraud occurrence."
)

# ==========================================================
# Transaction Type Chart
# ==========================================================

section_title("Fraud Rate by Transaction Type")

display_image(
    "images/fraud_by_transaction_type.png",
    "Fraud Rate by Transaction Type"
)

# ==========================================================
# Interpretation
# ==========================================================

display_analysis(

    findings=[

        "The fraud rate is very similar across all transaction types.",

        "Transfer transactions show the highest fraud rate (3.63%).",

        "Payment transactions show the lowest fraud rate (3.56%).",

        "The differences remain very small."

    ],

    insight="""
Fraudsters do not appear to target a specific transaction type.
The fraud distribution is relatively uniform across all categories.
""",

    conclusion="""
Transaction type alone is not a strong predictor of fraudulent activity
and should be combined with other behavioural variables.
"""
)