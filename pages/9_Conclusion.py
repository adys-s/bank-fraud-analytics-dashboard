# ==========================================================
# PROJECT CONCLUSION
# ==========================================================

import streamlit as st

from utils import page_title

page_title(
    "Project Conclusion",
    "Summary of the exploratory analysis."
)

st.subheader("Main Findings")

st.markdown("""

- The dataset contains **5 million banking transactions**.

- Fraud represents **3.59%** of all transactions.

- Most variables show very similar fraud rates.

- No individual variable clearly identifies fraudulent transactions.

- Behavioural variables must be combined to improve fraud detection.

""")

st.subheader("Next Steps")

st.markdown("""

- Develop Machine Learning models.

- Compare several classification algorithms.

- Improve feature engineering.

- Deploy predictive models on Microsoft Azure.

""")

st.success("The exploratory analysis provides a solid foundation for building fraud detection models.")