# ==========================================================
# MERCHANT CATEGORY ANALYSIS
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
    "Merchant Category Analysis",
    "This section analyses fraud rates across different merchant categories."
)

# ==========================================================
# Merchant Category Chart
# ==========================================================

section_title("Fraud Rate by Merchant Category")

display_image(
    "images/fraud_by_merchant_category.png",
    "Fraud Rate by Merchant Category"
)

# ==========================================================
# Interpretation
# ==========================================================

display_analysis(

    findings=[

        "Fraud rates remain very similar across all merchant categories.",

        "Entertainment and Other categories show the highest fraud rate (3.61%).",

        "Utilities show the lowest fraud rate (3.57%).",

        "No category clearly stands out."

    ],

    insight="""
Merchant category alone provides limited information for identifying
fraudulent transactions.
""",

    conclusion="""
Merchant category should be combined with behavioural and temporal
features to improve fraud detection.
"""
)