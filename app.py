import streamlit as st
import requests

WEBHOOK = "PASTE_WEBHOOK_URL"

# ======================
# TOOL HEADER
# ======================

st.title("Madison Market Insight Tool")

st.write(
    "Analyzes real product launches and hiring data to generate structured market insights."
)

# ======================
# INPUTS
# ======================

st.header("Input")

brand = st.text_input(
    "Brand or Market Focus",
    placeholder="Example: Nike, AI startups, Fintech tools"
)

goal = st.text_area(
    "Analysis Goal",
    placeholder="Example: Identify marketing trends and hiring demand signals"
)

run = st.button("Run Analysis")

# ======================
# VALIDATION
# ======================

if run:

    if not brand.strip():
        st.error("Brand/Market focus is required.")
        st.stop()

    payload = {
        "brand": brand,
        "goal": goal
    }

    with st.spinner("Running analysis..."):

        try:
            res = requests.post(WEBHOOK, json=payload)
            data = res.json()
        except:
            st.error("Could not connect to analysis engine.")
            st.stop()

    # ======================
    # OUTPUT
    # ======================

    st.header("Results")

    report = data.get("output") or data.get("text") or str(data)

    st.markdown(report)

    # Highlight section
    st.subheader("Key Insight Highlight")
    st.info("Analysis generated from real launch and job-market data sources.")

# ======================
# BASIC INFO SECTION
# ======================

st.header("About")

st.write("""
**What it does:**  
Analyzes real-world brand announcements, product launches, and marketing posts to detect trends, positioning patterns, and workforce demand.

**Who it's for:**  
Marketers, founders, analysts, and researchers.

**Tech Stack:**  
n8n workflow · APIs · Data pipelines · LLM analysis

**Created by:** Guna R  
**Portfolio:** https://yourportfolio.com
""")
