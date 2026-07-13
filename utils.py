# ==========================================================
# UTILITY FUNCTIONS
# Bank Fraud Analytics Dashboard
# ==========================================================

# ==========================
# Import libraries
# ==========================

import streamlit as st


# ==========================================================
# FUNCTION : Display page title
# ==========================================================

def page_title(title, description):
    """
    Display the page title and a short description.

    Parameters
    ----------
    title : str
        Main title of the page.

    description : str
        Short description displayed below the title.
    """

    st.title(title)

    st.write(description)

    st.divider()


# ==========================================================
# FUNCTION : Display an image
# ==========================================================

def display_image(image_path, caption=None):
    """
    Display an image using the full page width.

    Parameters
    ----------
    image_path : str
        Path of the image.

    caption : str, optional
        Image caption.
    """

    st.image(
        image_path,
        caption=caption,
        use_container_width=True
    )


# ==========================================================
# FUNCTION : Display analysis
# ==========================================================

def display_analysis(findings, insight, conclusion):
    """
    Display the interpretation of a graph.

    Parameters
    ----------
    findings : list
        List of key findings.

    insight : str
        Business insight.

    conclusion : str
        Final conclusion.
    """

    st.subheader("Key Findings")

    for finding in findings:
        st.markdown(f"- {finding}")

    st.subheader("Business Insight")

    st.info(insight)

    st.subheader("Conclusion")

    st.success(conclusion)

    st.divider()


# ==========================================================
# FUNCTION : Display section title
# ==========================================================

def section_title(title):
    """
    Display a section title.

    Parameters
    ----------
    title : str
        Section title.
    """

    st.header(title)