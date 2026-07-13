# ==========================================================
# VELOCITY SCORE ANALYSIS
# ==========================================================

from utils import page_title, section_title, display_image, display_analysis

page_title(
    "Velocity Score Analysis",
    "Analysis of customer transaction velocity."
)

# ==========================================================
# Velocity Histogram
# ==========================================================

section_title("Velocity Score Distribution")

display_image(
    "images/10_velocity_histogram.png",
    "Velocity Score Distribution"
)

display_analysis(

    findings=[
        "Velocity scores follow similar distributions.",
        "Fraudulent and legitimate transactions largely overlap.",
        "No obvious separation is observed."
    ],

    insight="""
Velocity score alone provides limited predictive power.
""",

    conclusion="""
Velocity should be combined with behavioural features
to improve fraud detection.
"""
)

# ==========================================================
# Velocity Boxplot
# ==========================================================

section_title("Velocity Score Boxplot")

display_image(
    "images/09_velocity_boxplot.png",
    "Velocity Score Boxplot"
)

display_analysis(

    findings=[
        "Median velocity scores are almost identical for both classes.",
        "The variability remains very similar between legitimate and fraudulent transactions."
    ],

    insight="""
The boxplot confirms that fraudulent transactions do not exhibit a distinct
velocity pattern compared to legitimate transactions.
""",

    conclusion="""
Velocity score alone is not sufficient to identify fraudulent transactions
and should be combined with additional behavioural indicators.
"""
)