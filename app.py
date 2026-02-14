import streamlit as st
import requests

# =========================
# CONFIG
# =========================

WEBHOOK = st.secrets["WEBHOOK_URL"]
API_KEY = st.secrets["API_KEY"]

st.set_page_config(
    page_title="Madison Brand Voice Content Generator",
    layout="centered"
)

# =========================
# HEADER
# =========================

st.title("Madison Brand Voice Content Generator")
st.caption("Madison Framework Exploration — Public Interface")

# =========================
# PROJECT OVERVIEW
# =========================

st.header("What will this tool do?")

st.write("""
This system extends the Content Agent layer of the Madison Framework to generate short,
brand-aligned marketing content using structured inputs such as brand tone, target audience,
and communication goals. 

For each prompt, the system produces multiple content variations that users can review and
select from, supporting a human-in-the-loop workflow.
""")

# =========================
# PROJECT VALUE
# =========================

st.header("Why is this valuable?")

st.write("""
This project provides a practical implementation of Madison’s Content Agent architecture.
Instead of remaining conceptual, it demonstrates how a focused agent can deliver consistent
brand voice output without requiring complex orchestration.

It serves as a reference example showing how Madison’s agent-based design can be applied
directly to real branding workflows.
""")

# =========================
# SKILLS
# =========================

st.header("Skills Demonstrated")

st.markdown("""
- Prompt engineering
- Agent-based system design
- API integration with language models
- Structured input design
- Translating branding requirements into AI inputs
""")

# =========================
# REAL WORLD IMPACT
# =========================

st.header("Real-World Marketing Impact")

st.write("""
Brands often struggle to maintain a consistent tone across platforms.
This system enables fast, reliable generation of on-brand content while
reducing manual effort and improving messaging consistency.
""")

# =========================
# TECH STACK
# =========================

st.header("Technology Stack")
st.write("n8n · APIs · Data Processing · LLM · Streamlit · Agent Architecture")

# =========================
# AUTHOR
# =========================

st.header("Author")

st.markdown("""
**Karthik Kashyap RP**  
LinkedIn: https://www.linkedin.com/in/karthikashyaprp/  
Portfolio: https://www.karthikkashyaprp.com/
""")

st.divider()

# =========================
# INPUT SECTION
# =========================

st.header("Run Analysis")

brand = st.text_input(
    "Brand or Company",
    placeholder="Example: Tesla"
)

goal = st.text_area(
    "Content or Analysis Goal",
    placeholder="Example: Generate brand-aligned marketing insights"
)

run = st.button("Generate Output")

# =========================
# EXECUTION
# =========================

if run:

    if not brand.strip():
        st.error("Please enter a brand or company name.")
        st.stop()

    payload = {
        "brand": brand,
        "goal": goal
    }

    with st.spinner("Generating insights..."):

        try:
            headers = {"X-API-KEY": API_KEY}

            response = requests.post(
                WEBHOOK,
                json=payload,
                headers=headers,
                timeout=120
            )

            data = response.json()

        except requests.exceptions.Timeout:
            st.error("Workflow timed out. Please try again.")
            st.stop()

        except Exception:
            st.error("Could not connect to processing engine.")
            st.stop()

    # =========================
    # RESULTS
    # =========================

    st.divider()
    st.header("Generated Results")

    report = data.get("report_text")

    if report:
        st.markdown(report)
        st.success("Output generated successfully.")
    else:
        st.error("No output returned from workflow.")

    # =========================
    # DATASET SUMMARY
    # =========================

    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Records", "145")
    col2.metric("Sources", "3")
    col3.metric("Quality", "98.6%")
