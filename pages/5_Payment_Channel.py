# ==========================================================
# PAYMENT CHANNEL ANALYSIS
# ==========================================================

from utils import page_title, section_title, display_image, display_analysis

page_title(
    "Payment Channel Analysis",
    "Analysis of fraud rates across payment channels."
)

section_title("Fraud Rate by Payment Channel")

display_image(
    "images/fraud_by_payment_channel.png",
    "Fraud Rate by Payment Channel"
)

display_analysis(

    findings=[
        "Fraud rates remain similar across payment channels.",
        "Wire Transfer has the highest fraud rate (3.60%).",
        "ACH has the lowest fraud rate (3.58%).",
        "Differences remain negligible."
    ],

    insight="""
Fraudsters appear to use every payment channel.
""",

    conclusion="""
Payment channel alone cannot effectively identify fraud.
"""
)