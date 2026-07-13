# ==========================================================
# DEVICE USED ANALYSIS
# ==========================================================

from utils import page_title, section_title, display_image, display_analysis

page_title(
    "Device Used Analysis",
    "Analysis of fraud rates by device type."
)

section_title("Fraud Rate by Device")

display_image(
    "images/fraud_by_device.png",
    "Fraud Rate by Device"
)

display_analysis(

    findings=[
        "ATM transactions have the highest fraud rate (3.62%).",
        "Mobile transactions have the lowest fraud rate (3.57%).",
        "Differences are very small."
    ],

    insight="""
No device category clearly distinguishes fraudulent behaviour.
""",

    conclusion="""
Device type should be combined with other fraud indicators.
"""
)