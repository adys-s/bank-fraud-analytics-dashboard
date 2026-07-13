# ==========================================================
# BANK FRAUD ANALYTICS DASHBOARD
# Author : Yawa Silvère ADODO-DAHOUE
# ==========================================================

import streamlit as st
from PIL import Image

# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Bank Fraud Analytics Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# CSS
# ----------------------------------------------------------

st.markdown("""
<style>

/* Fond */
.stApp{
    background-color:#0E1117;
}

/* Titre */
.title{
    color:#4F8BF9;
    font-size:48px;
    font-weight:bold;
    text-align:center;
}

/* Sous-titre */

.subtitle{
    color:#B8C1CC;
    font-size:20px;
    text-align:center;
}

/* Titres */

.section{
    color:#4F8BF9;
    font-size:28px;
    font-weight:bold;
}

/* Footer */

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}

</style>

""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

logo = Image.open("assets/logo.png")

st.sidebar.image(logo, use_container_width=True)

st.sidebar.markdown("---")

st.sidebar.success("Bank Fraud Analytics Dashboard")

st.sidebar.caption(
"""
Exploratory Data Analysis

5 Million Transactions

Python • Streamlit • Azure
"""
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Use the navigation menu to explore
the different analyses.
"""
)

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------

st.markdown(
"""
<div class='title'>

BANK FRAUD ANALYTICS

</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='subtitle'>

Data • Insight • Security

</div>
""",
unsafe_allow_html=True
)

st.divider()

# ----------------------------------------------------------
# Key Metrics
# ----------------------------------------------------------

st.markdown(
"<p class='section'>Key Metrics</p>",
unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Transactions",
    "5,000,000"
)

col2.metric(
    "Fraud Cases",
    "179,553"
)

col3.metric(
    "Fraud Rate",
    "3.59%"
)

col4.metric(
    "Dataset Year",
    "2023"
)

st.divider()

# ----------------------------------------------------------
# Project Overview
# ----------------------------------------------------------

st.markdown(
"<p class='section'>Project Overview</p>",
unsafe_allow_html=True
)

st.write("""
This dashboard presents the results of an **Exploratory Data Analysis (EDA)**
performed on a banking dataset containing **5 million transactions**.

The objective is to analyse transaction behaviour, identify fraud patterns
and prepare the dataset for future **Machine Learning** applications.

This project was developed using **Python, Pandas, Streamlit and Microsoft Azure**.
""")

st.divider()

# ----------------------------------------------------------
# Project Objectives
# ----------------------------------------------------------

st.markdown(
"<p class='section'>Project Objectives</p>",
unsafe_allow_html=True
)

st.markdown("""
- Explore transaction behaviour
- Identify fraud indicators
- Build meaningful visualisations
- Prepare Machine Learning features
- Develop an interactive dashboard
- Deploy the application on Microsoft Azure
""")

st.divider()

# ----------------------------------------------------------
# Technology Stack
# ----------------------------------------------------------

st.markdown(
"<p class='section'>Technology Stack</p>",
unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

c1.success("Python")

c2.success("Pandas")

c3.success("Streamlit")

c4.success("Microsoft Azure")

st.divider()

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.markdown(
"""
<div class="footer">

Developed by Yawa Silvere ADODO-DAHOUE</b>

Data Analytics Portfolio Project

</div>
""",
unsafe_allow_html=True
)