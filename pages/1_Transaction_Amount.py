# ==========================================================
# TRANSACTION AMOUNT ANALYSIS
# ==========================================================

# ==========================
# Import libraries
# ==========================

from utils import *

# ==========================================================
# Page title
# ==========================================================

page_title(
    "Transaction Amount",
    "Analysis of transaction amount distribution."
)

# ==========================================================
# Histogram
# ==========================================================

section_title("Transaction Amount Distribution")

display_image(
    "images/amount_histogram.png"
)

display_analysis(

    findings=[

        "Most transactions involve relatively small amounts.",

        "The distribution is highly right-skewed.",

        "Large transactions are uncommon."

    ],

    insight="""
Transaction amount alone is not sufficient
to distinguish fraudulent transactions.
""",

    conclusion="""
This variable should be combined with
other behavioural variables.
"""
)

# ==========================================================
# Boxplot
# ==========================================================

section_title("Transaction Amount Boxplot")

display_image(
    "images/amount_boxplot.png"
)

display_analysis(

    findings=[

        "Several outliers are present.",

        "Fraudulent and legitimate transactions have similar distributions."

    ],

    insight="""
Extreme values exist in both classes.
""",

    conclusion="""
Transaction amount is not a strong standalone
fraud indicator.
"""
)