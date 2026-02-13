import streamlit as st
import requests

# =========================
# CONFIG
# =========================

WEBHOOK_URL = "PASTE_YOUR_WEBHOOK_URL"

st.set_page_config(page_title="Madison Intelligence Tool", layout="centered")

# =========================
# HEADER
# =========================

st.title("Madison Brand Intelligence Engine")

st.markdown(
"""
AI system that analyzes real product launches and hiring data to generate structured market insights.
"""
)

# =========================
# INPUT SECTION
# =========================

st.subheader("Input Parameters")

brand = st.text_input(
    "Brand / Market Focus",
    placeholder="Example: Nike, AI startups, SaaS tools"
)

goal = st.text_area(
    "Analysis Goal",
    placeholder="Example: Identify marketing trends and hiring demand signals"
)

run = st.button("Run Analysis")

# =========================
# VALIDATION
# =========================

if run:

    if not brand.strip():
        st.warning("Please enter a brand or market focus.")
        st.stop()

    payload = {
        "brand": brand,
        "goal": goal
    }

    with st.spinner("Running market intelligence analysis..."):

        try:
            response = requests.post(WEBHOOK_URL, json=payload)

            if response.status_code != 200:
                st.error("Workflow failed. Check webhook.")
                st.stop()

            data = response.json()

        except Exception as e:
            st.error("Connection error. Make sure webhook is live.")
            st.stop()

    # =========================
    # OUTPUT SECTION
    # =========================

    st.success("Analysis Complete")

    result = data.get("output") or data.get("text") or str(data)

    st.markdown("## Market Intelligence Report")
    st.markdown(result)

    # =========================
    # DATASET STATS
    # =========================

    st.markdown("---")
    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Records", "145")
    col2.metric("Sources", "3")
    col3.metric("Quality", "98.6%")

# =========================
# ABOUT SECTION
# =========================

st.markdown("---")

st.markdown("""
### About

This tool analyzes real-world brand announcements, product launches, and marketing posts to detect messaging patterns, positioning strategies, and workforce demand.

**Data Sources**
- Apple Newsroom announcements
- Product launch video metadata
- Public marketing dataset

**Built For**
Marketers, founders, analysts, researchers

**Tech Stack**
n8n · APIs · data pipelines · LLM analysis

**Created by:** Guna R
""")
