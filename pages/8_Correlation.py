# ==========================================================
# CORRELATION MATRIX
# ==========================================================

from utils import page_title, section_title, display_image, display_analysis

page_title(
    "Correlation Matrix",
    "Analysis of relationships between numerical variables."
)

section_title("Correlation Heatmap")

display_image(
    "images/correlation_matrix.png",
    "Correlation Matrix"
)

display_analysis(

    findings=[
        "No variable is strongly correlated with fraud.",
        "Most correlations remain weak.",
        "Behavioural variables appear independent."
    ],

    insight="""
Fraud detection cannot rely on a single variable.
""",

    conclusion="""
Machine Learning models will need to combine several variables.
"""
)