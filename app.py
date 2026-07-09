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
        placeholder="e.g., Paris Saint-Germain, EuroLeague Basketball, Formula 1...",
    )
    
with col2:
    # Security Token handling (Hidden or environment-backed)
    api_key_input = st.text_input(
        "ADVISORY ACCESS TOKEN :", 
        type="password", 
        placeholder="Enter credentials...",
        help="Required for dynamic generation."
    )

# Strict Corporate System Instructions
SYSTEM_INSTRUCTIONS = """
You are an elite Sport Business M&A Analyst. 
Generate a comprehensive, highly aesthetic, static HTML slide deck based on the user's requested sports asset.
The language of the deck MUST be strictly English.

Visual Identity constraints (Consulting White Theme):
- Each slide must be enclosed in its own `<div class="slide-container">` with dimensions of exactly `1280px` wide by `720px` high.
- Background: `#ffffff` with professional margins.
- Colors: `#0F172A` (deep navy for headers), `#2563EB` (electric blue for accents), `#F8FAFC` (light grey cards), `#E2E8F0` (borders).
- Fonts: Inter / Poppins via Google Fonts.
- Contents: Title Slide, Market & Media Rights Context, Valuation Analytics, and Strategic Roadmap.

Data Integrity rule:
- DO NOT invent or extrapolate non-public financial metrics. If data is unknown, use "Data Room Verification Required" or label clearly as "Indicative Advisory Assessment".
"""

# Premium English Base Template
CLEAN_ENG_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Poppins:wght@600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background-color: #0B0F19; display: flex; flex-direction: column; align-items: center; gap: 30px; padding: 40px; }
        .slide-container {
            width: 1280px; height: 720px; background: #ffffff; border-radius: 4px;
            padding: 60px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden;
            font-family: 'Inter', sans-serif; color: #0F172A;
        }
        .slide-container::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 6px; background-color: #2563EB; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #F1F5F9; padding-bottom: 20px; }
        .brand { font-family: 'Poppins', sans-serif; font-size: 16px; font-weight: 700; color: #0F172A; }
        .brand b { color: #2563EB; }
        .slide-title { font-family: 'Poppins', sans-serif; font-size: 38px; color: #0F172A; margin-top: 20px; }
        .content { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 40px; flex-grow: 1; align-items: center; margin-top: 20px; }
        p { font-size: 16px; color: #4B5563; line-height: 1.6; }
        .card { background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 30px; border-radius: 4px; }
        .kpi-num { font-size: 44px; font-weight: 800; color: #2563EB; letter-spacing: -1px; }
        .footer { display: flex; justify-content: space-between; font-size: 11px; color: #94A3B8; font-weight: 500; text-transform: uppercase; border-top: 1px solid #F1F5F9; padding-top: 20px; }
    </style>
</head>
<body>

<div class="slide-container">
    <div class="header">
        <div class="brand">inthe<b>boardroom</b> / Advisory</div>
        <div style="font-size:11px; color:#64748B; font-weight:700; letter-spacing:1px;">STRICTLY CONFIDENTIAL</div>
    </div>
    <div class="content" style="grid-template-columns: 1fr; text-align:center;">
        <div style="padding: 60px 0;">
            <p style="color:#2563EB; font-weight:700; letter-spacing:3px; text-transform:uppercase; margin-bottom:15px;">Strategic Asset Profile</p>
            <h1 style="font-family:'Poppins'; font-size:64px; color:#0F172A; letter-spacing:-1px;">TARGET: {ASSET_NAME}</h1>
            <div style="width:60px; height:4px; background:#2563EB; margin:30px auto;"></div>
            <p style="font-size:18px; max-width:700px; margin: 0 auto; color:#64748B;">Preliminary investment memorandum and premium commercial positioning overview.</p>
        </div>
    </div>
    <div class="footer"><span>Advisory Work Material</span><span>Slide 1</span></div>
</div>

</body>
</html>
"""

if st.button("🚀 GENERATE INVESTMENT MEMORANDUM DECK"):
    # Target resolution logic
    target_asset = subject.strip() if subject.strip() else "Selected Sports Property"
    
    with st.spinner("Processing asset analytics..."):
        # Prioritize live API key if provided, or fallback to secure environment config
        final_api_key = api_key_input.strip() if api_key_input.strip() else os.environ.get("ANTHROPIC_API_KEY")
        
        if final_api_key:
            try:
                client = Anthropic(api_key=final_api_key)
                prompt_payload = f"Generate an executive M&A slide deck for {target_asset}. Ensure clean layout, high density financial tables or structured charts where appropriate."
                
                message = client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=4000,
                    system=SYSTEM_INSTRUCTIONS,
                    messages=[{"role": "user", "content": prompt_payload}]
                )
                html_result = message.content[0].text
            except Exception as e:
                st.error(f"Execution Error: {e}")
                html_result = CLEAN_ENG_TEMPLATE.replace("{ASSET_NAME}", target_asset.upper())
        else:
            # Clean instant placeholder to show user layout capability without failing
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