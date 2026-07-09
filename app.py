import streamlit as st
import streamlit.components.v1 as components
from anthropic import Anthropic
import os

# Premium Wall Street / London Executive Configuration
st.set_page_config(
    page_title="In The Boardroom | Intelligence Platform",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom High-End Minimalist CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #0B0F19 !important;
        color: #E2E8F0 !important;
    }
    .stTextInput input {
        background-color: #111827 !important;
        border: 1px solid #1F2937 !important;
        color: #FFFFFF !important;
        border-radius: 4px !important;
        padding: 0.75rem !important;
    }
    .stButton>button {
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 4px !important;
        font-weight: 500 !important;
        letter-spacing: 0.5px;
        padding: 0.75rem 2rem !important;
        border: none !important;
        width: 100%;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #3B82F6 !important;
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.4);
    }
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    .reportview-container .main .footer {
        text-align: center;
        color: #4B5563;
        font-size: 12px;
        margin-top: 60px;
    }
    div[data-testid="stMarkdownContainer"] p {
        color: #9CA3AF;
    }
</style>
""", unsafe_allow_html=True)

# Main Terminal Interface Header
st.title("💼 In The Boardroom")
st.markdown("### **M&A Asset Advisory & Deck Intelligence Engine**")
st.markdown("---")

# Layout Form
col1, col2 = st.columns([2, 1])

with col1:
    subject = st.text_input(
        "ENTER TARGET ASSET (Club, League, or Sports Property):",
        placeholder="e.g., Paris Saint-Germain, Stade Brestois, Manchester United...",
    )
    
with col2:
    api_key_input = st.text_input(
        "ADVISORY ACCESS TOKEN :", 
        type="password", 
        placeholder="Enter credentials...",
        help="Required for dynamic generation."
    )

# Elite M&A Corporate System Instructions
SYSTEM_INSTRUCTIONS = """
You are an elite, top-tier Sport Business M&A Analyst working for a major investment bank in London/New York. 
Your task is to generate a comprehensive, highly aesthetic, multi-slide investment memorandum HTML deck based on the requested sports asset.
The language of the deck MUST be strictly professional, corporate English.

Visual Identity constraints (High-End Consulting Theme):
- Return ONLY the valid HTML code starting with `<!DOCTYPE html>` and ending with `</html>`. No preamble, no conversational text.
- Every single slide must be enclosed in its own `<div class="slide-container">` block. 
- Layout Dimensions: exactly 1280px wide by 720px high for each slide.
- Style: Background `#ffffff`, deep navy headers (`#0F172A`), electric blue accents (`#2563EB`), clear borders (`#E2E8F0`). Use clean professional tables, metric cards, and 2-column executive summaries.
- Typography: Use 'Inter' or 'Poppins' from Google Fonts. Keep it clean and readable.

Content & Deck Structure requirements:
- Generate a robust, multi-page deck (minimum 4 distinct slides/sections within the HTML).
- Slide 1: Premium Title Slide (Asset Name, Context, Confidentiality Banner).
- Slide 2: Market & Commercial Revenue Analysis (Broadcasting/Media Rights landscape, Commercial sponsorship growth, Matchday dynamics).
- Slide 3: M&A Valuation Analytics & Comparables (Provide precise valuation frameworks: revenue multiples, enterprise value indications, asset-backed analysis. If metrics are non-public, use professional advisory estimates labeled as 'Indicative Advisory Assessment').
- Slide 4: Strategic Roadmap & Investment Highlights (Internationalization, Infrastructure opportunities, Digital scaling).

Data Integrity rule:
- Deliver extremely sharp, detailed financial and business insights. Avoid generic text. Act as a seasoned sports investment banker.
"""

# Clean English Base Template (Fallback)
CLEAN_ENG_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Poppins:wght@600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background-color: #0B0F19; display: flex; flex-direction: column; align-items: center; gap: 40px; padding: 40px; }
        .slide-container {
            width: 1280px; height: 720px; background: #ffffff; border-radius: 4px;
            padding: 60px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden;
            font-family: 'Inter', sans-serif; color: #0F172A; margin-bottom: 30px;
        }
        .slide-container::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 6px; background-color: #2563EB; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #F1F5F9; padding-bottom: 20px; }
        .brand { font-family: 'Poppins', sans-serif; font-size: 16px; font-weight: 700; color: #0F172A; }
        .brand b { color: #2563EB; }
        .slide-title { font-family: 'Poppins', sans-serif; font-size: 38px; color: #0F172A; margin-top: 20px; }
        .content { display: grid; grid-template-columns: 1fr; text-align: center; flex-grow: 1; align-items: center; margin-top: 20px; }
        p { font-size: 16px; color: #4B5563; line-height: 1.6; }
        .footer { display: flex; justify-content: space-between; font-size: 11px; color: #94A3B8; font-weight: 500; text-transform: uppercase; border-top: 1px solid #F1F5F9; padding-top: 20px; }
    </style>
</head>
<body>

<div class="slide-container">
    <div class="header">
        <div class="brand">inthe<b>boardroom</b> / Advisory</div>
        <div style="font-size:11px; color:#64748B; font-weight:700; letter-spacing:1px;">STRICTLY CONFIDENTIAL</div>
    </div>
    <div class="content">
        <div style="padding: 60px 0;">
            <p style="color:#2563EB; font-weight:700; letter-spacing:3px; text-transform:uppercase; margin-bottom:15px;">Strategic Asset Profile</p>
            <h1 style="font-family:'Poppins'; font-size:64px; color:#0F172A; letter-spacing:-1px;">TARGET: {ASSET_NAME}</h1>
            <div style="width:60px; height:4px; background:#2563EB; margin:30px auto;"></div>
            <p style="font-size:18px; max-width:700px; margin: 0 auto; color:#64748B;">Please check API Configuration or Secret tokens to enable full AI M&A multi-slide generation.</p>
        </div>
    </div>
    <div class="footer"><span>Advisory Work Material</span><span>Slide 1</span></div>
</div>

</body>
</html>
"""

if st.button("🚀 GENERATE INVESTMENT MEMORANDUM DECK"):
    target_asset = subject.strip() if subject.strip() else "Selected Sports Property"
    
    with st.spinner("Processing deep financial & asset analytics..."):
        # Prioritize live input token, fallback to Streamlit Secrets
        final_api_key = api_key_input.strip() if api_key_input.strip() else st.secrets.get("ANTHROPIC_API_KEY")
        
        if final_api_key:
            try:
                client = Anthropic(api_key=final_api_key)
                prompt_payload = f"Generate a full, highly analytical executive M&A slide deck for {target_asset}. Ensure high density financial tables, market positioning charts, commercial rights insights, and strategic roadmap slides. Keep everything in perfect HTML structure."
                
                message = client.messages.create(
                    model="claude-3-5-sonnet-latest",
                    max_tokens=4000,
                    system=SYSTEM_INSTRUCTIONS,
                    messages=[{"role": "user", "content": prompt_payload}]
                )
                html_result = message.content[0].text
            except Exception as e:
                st.error(f"Execution Error: {e}")
                html_result = CLEAN_ENG_TEMPLATE.replace("{ASSET_NAME}", target_asset.upper())
        else:
            html_result = CLEAN_ENG_TEMPLATE.replace("{ASSET_NAME}", target_asset.upper())

        # Render Interface Results
        st.markdown("### **Executive Preview**")
        components.html(html_result, height=760, scrolling=True)
        
        st.download_button(
            label="📥 EXPORT RAW HTML DECK",
            data=html_result,
            file_name=f"boardroom_deck_{target_asset.lower().replace(' ', '_')}.html",
            mime="text/html"
        )

st.markdown("""
<div class="footer">
    <p>In The Boardroom • Institutional Platform © 2026</p>
</div>
""", unsafe_allow_html=True)