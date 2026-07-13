# ==========================================================
# LOCATION ANALYSIS
# ==========================================================

from utils import page_title, section_title, display_image, display_analysis

page_title(
    "Location Analysis",
    "Analysis of fraud rates across different cities."
)

section_title("Fraud Rate by Location")

display_image(
    "images/fraud_by_location.png",
    "Fraud Rate by Location"
)

display_analysis(

    findings=[
        "Fraud rates are remarkably similar across all cities.",
        "London and Toronto show the highest fraud rate (3.60%).",
        "Tokyo and Dubai show the lowest fraud rate (3.58%).",
        "Geographical differences are minimal."
    ],

    insight="""
Location alone does not appear to be a significant fraud indicator.
""",

    conclusion="""
Location should be combined with additional behavioural variables.
"""
)