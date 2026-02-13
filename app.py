import streamlit as st
import requests



# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.title("Madison Brand Voice Generator")

st.write(
    "Interactive AI system that studies real brand messaging and generates structured marketing intelligence."
)

st.divider()

# ------------------------------------------------
# SYSTEM OVERVIEW
# ------------------------------------------------

st.header("System Overview")

st.markdown("""
This tool analyzes real-world launch messaging and promotional content to understand how brands communicate.

It combines:
- announcement language
- marketing tone patterns
- hiring demand signals

The system then produces structured insights designed for strategic decision-making.
""")

# ------------------------------------------------
# USERS
# ------------------------------------------------

st.header("Intended Users")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- Startup founders  
- Product managers  
- Growth teams  
""")

with col2:
    st.markdown("""
- Marketing analysts  
- Strategy teams  
- Researchers  
""")

# ------------------------------------------------
# TECH DETAILS
# ------------------------------------------------

st.header("Technical Framework")

st.write("""
Pipeline: n8n automated workflow  
Sources: RSS + APIs + structured datasets  
Processing: normalization + filtering + aggregation  
Analysis: LLM reasoning engine  
Interface: Streamlit public UI
""")

# ------------------------------------------------
# INPUT PANEL
# ------------------------------------------------

st.header("Run Analysis")

brand = st.text_input(
    "Target Brand or Industry",
    placeholder="Example: Apple, AI tools, SaaS platforms"
)

goal = st.text_area(
    "What insight are you looking for?",
    placeholder="Example: Identify messaging trends and hiring demand"
)

run = st.button("Generate Intelligence")

# ------------------------------------------------
# VALIDATION + EXECUTION
# ------------------------------------------------

if run:

    if not brand.strip():
        st.warning("Please enter a brand or industry.")
        st.stop()

    payload = {"brand": brand, "goal": goal}

    with st.spinner("Processing market signals..."):

        try:
            response = requests.post(WEBHOOK, json=payload)
            data = response.json()
        except:
            st.error("Unable to reach analysis engine.")
            st.stop()

    # ------------------------------------------------
    # OUTPUT
    # ------------------------------------------------

    st.divider()
    st.header("Analysis Output")

    result = data.get("output") or data.get("text") or str(data)

    st.markdown(result)

    st.info("Generated using real launch + workforce datasets.")

# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.divider()

st.caption("""
Author: Karthik Kashyap RP 
LinkedIn: http://karthikkashyaprp.com/
""")
