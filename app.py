import streamlit as st
import requests

# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="Madison Intelligence",
    page_icon="📊",
    layout="centered"
)

WEBHOOK = "PASTE_YOUR_WEBHOOK_URL"

# ======================
# STYLE
# ======================

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.title {
    font-size:42px;
    font-weight:700;
    text-align:center;
}

.subtitle {
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:40px;
}

.section {
    background-color:#111827;
    padding:25px;
    border-radius:12px;
    margin-bottom:20px;
}

.metric-card {
    background:#111827;
    padding:18px;
    border-radius:12px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================

st.markdown('<div class="title">Madison Intelligence Engine</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">AI-powered market analysis using real launch + hiring data</div>',
    unsafe_allow_html=True
)

# ======================
# INPUT CARD
# ======================

with st.container():

    st.markdown("### Input Parameters")

    brand = st.text_input(
        "Brand / Market Focus",
        placeholder="Nike, AI startups, Fintech tools"
    )

    goal = st.text_area(
        "Analysis Goal",
        placeholder="Identify marketing trends and hiring demand"
    )

    run = st.button("Generate Insights", use_container_width=True)

# ======================
# RUN ANALYSIS
# ======================

if run:

    if not brand.strip():
        st.warning("Enter a brand or market focus")
        st.stop()

    payload = {"brand": brand, "goal": goal}

    with st.spinner("Analyzing real market data..."):

        try:
            res = requests.post(WEBHOOK, json=payload)
            data = res.json()
        except:
            st.error("Webhook not reachable")
            st.stop()

    result = data.get("output") or data.get("text") or str(data)

    st.markdown("---")
    st.markdown("## 📊 Analysis Report")
    st.markdown(result)

# ======================
# DATASET METRICS
# ======================

st.markdown("---")
st.markdown("### Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Records", "145")

with col2:
    st.metric("Sources", "3")

with col3:
    st.metric("Quality", "98.6%")

# ======================
# ABOUT
# ======================

with st.expander("About this tool"):

    st.markdown("""
**Madison Intelligence Engine** analyzes real-world marketing content to detect patterns in messaging, positioning, and hiring demand.

**Data Sources**
- Apple announcements
- Product launch videos
- Marketing datasets

**Built for**
Marketers · Analysts · Founders · Researchers

**Tech Stack**
n8n · APIs · LLMs · Data Pipelines

**Creator**
Guna R
""")
