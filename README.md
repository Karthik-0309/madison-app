# Madison Brand Voice Generator

Public interface for Assignment 5 AI workflow  
Author: Karthik Kashyap RP  

---

## Overview
Madison Brand Voice Generator is an AI-powered tool that analyzes marketing language patterns and generates structured brand voice insights. It helps users quickly understand how a brand communicates — including tone, messaging style, personality, and value themes — using real-world content data.

The system is designed for non-technical users and runs through a simple web interface.

---

## What This Tool Does
- Analyzes marketing content language
- Detects tone patterns
- Identifies messaging style
- Infers brand personality traits
- Extracts recurring value themes
- Generates structured voice recommendations

---

## Who It’s For
- Founders
- Marketing teams
- Product teams
- Brand strategists
- Analysts
- Students learning marketing or branding

---

## Tech Stack
- Streamlit (UI)
- n8n (Workflow automation)
- APIs (Data ingestion)
- LLM (Language analysis)
- JSON processing pipeline

---

## How It Works (Architecture)

User Input → Streamlit Interface  
→ Webhook Request  
→ n8n Workflow  
→ Data Processing + Normalization  
→ Prompt Builder  
→ AI Model Analysis  
→ Structured Output Formatter  
→ Results Displayed to User  

---

## Inputs
Users only need to provide:

**Brand / Company**  
Example: `Nike`

**Goal**  
Example: `Analyze tone and messaging style`

No technical knowledge is required.

---

## Output
The system returns a structured report containing:

- Executive Summary
- Tone Patterns
- Messaging Style
- Brand Personality
- Value Themes
- Voice Recommendations

All results are formatted for readability and decision-making.

---

## Data Sources
The system analyzes real marketing content collected from:

- Brand announcement feeds
- Product launch messaging
- Structured marketing datasets
- Public promotional content

All data is normalized into a unified format before analysis.

---

## Validation + Reliability Controls
The workflow includes safeguards to ensure quality:

- Input validation before execution
- Structured prompt constraints
- Output format enforcement
- Token-safe data limits
- Error handling for API failures

---

## Deployment
The interface is publicly accessible and requires no login.  
It runs through a deployed Streamlit application connected to a live workflow endpoint.

---

## Example Use Case
A marketing analyst wants to understand how Nike communicates.

They enter:

Brand → Nike  
Goal → Analyze tone and messaging  

The system generates a structured brand voice analysis within seconds.

---

## Why This Project Matters
Maintaining consistent brand voice is difficult when content volume is high. This tool demonstrates how AI agents can assist marketing teams by automatically analyzing messaging patterns and producing clear insights.

It showcases how structured workflows combined with language models can deliver reliable, usable business intelligence.

---

## Future Improvements
Planned enhancements include:

- Downloadable reports
- Brand comparison mode
- Tone score visualization
- Suggested messaging improvements
- Multi-language support

---

## Author
**Karthik Kashyap RP**  
LinkedIn: https://www.linkedin.com/in/karthikashyaprp/  
Portfolio: https://www.karthikkashyaprp.com/

---

## License
This project is for academic and demonstration purposes.
