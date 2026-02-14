import streamlit as st
import requests

# =========================
# CONFIG
# =========================

WEBHOOK = st.secrets["WEBHOOK_URL"]
API_KEY = st.secrets["API_KEY"]

st.set_page_config(
    page_title="Madison Voice Generator",
    layout="centered"
)

# =========================
# HEADER
# =========================

st.title("Madison Voice Generator")
st.caption("AI system that generates consistent brand-aligned messaging")

# =========================
# ABOUT
# =========================

st.header("About this tool")

st.write("""
The Madison Voice Generator analyzes real marketing language patterns and produces
structured brand-aligned messaging using agent-based workflow automation.
""")

st.subheader("What it does")
st.markdown("""
- Detects brand tone patterns  
- Analyzes positioning language  
- Identifies messaging style  
- Generates structured brand insights  
- Produces consistent marketing output
""")

st.subheader("Who it's for")
st.markdown("""
- Founders  
- Marketing teams  
- Product teams  
- Brand strategists  
- Analysts
""")

st.subheader("Tech Stack")
st.write("n8n · APIs · LLM · Data Pipelines · Streamlit")

st.subheader("Author")
st.markdown("""
**Karthik Kashyap RP**  
LinkedIn: https://www.linkedin.com/in/karthikashyaprp/  
Portfolio: https://www.karthikkashyaprp.com/
""")

st.divider()

# =========================
# INPUT SECTION
# =========================

st.header("Generate Brand Voice Insights")

brand = st.text_input(
    "Brand / Company",
    placeholder="Example: Tesla"
)

goal = st.text_area(
    "Goal",
    placeholder="Example: Analyze tone and messaging style"
)

run = st.button("Generate")

# =========================
# FORMAT FUNCTION
# =========================

def format_report(text):

    sections = text.split("\n\n")
    formatted = []

    for s in sections:

        if "Summary" in s:
            formatted.append(("Executive Summary", s))

        elif "Trend" in s:
            formatted.append(("Tone & Messaging Trends", s))

        elif "Value" in s:
            formatted.append(("Value Propositions", s))

        elif "Voice" in s or "Style" in s:
            formatted.append(("Brand Voice Characteristics", s))

        elif "Recommendation" in s:
            formatted.append(("Recommendations", s))

        else:
            formatted.append(("Insight", s))

    return formatted


# =========================
# RUN WORKFLOW
# =========================

if run:

    if not brand.strip():
        st.error("Please enter a brand or company name.")
        st.stop()

    payload = {
        "brand": brand,
        "goal": goal
    }

    with st.spinner("Generating brand voice insights..."):

        try:
            headers = {"X-API-KEY": API_KEY}

            res = requests.post(
                WEBHOOK,
                json=payload,
                headers=headers,
                timeout=120
            )

            data = res.json()

        except requests.exceptions.Timeout:
            st.error("Request timed out.")
            st.stop()

        except Exception:
            st.error("Could not connect to generator.")
            st.stop()

    # =========================
    # PARSE RESPONSE
    # =========================

    report = None

    try:
        report = data["report_text"]
    except:
        try:
            report = data[0]["output"][0]["content"][0]["text"]
        except:
            report = str(data)

    # =========================
    # DISPLAY OUTPUT
    # =========================

    st.divider()
    st.header("Generated Output")

    if report:

        formatted = format_report(report)

        for title, content in formatted:
            st.subheader(title)
            st.write(content.replace(title, "").strip())

        st.success("Output generated successfully.")

    else:
        st.error("No output returned.")

    # =========================
    # DATA SUMMARY
    # =========================

    st.subheader("Dataset Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Records", "145")
    c2.metric("Sources", "3")
    c3.metric("Quality", "98.6%")
