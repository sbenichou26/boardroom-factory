import streamlit as st
import streamlit.components.v1 as components
from anthropic import Anthropic
import os
import base64

# Premium Wall Street / London Executive Configuration
st.set_page_config(
    page_title="In The Boardroom | Intelligence Platform",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom High-End Minimalist Dashboard Style
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
        placeholder="e.g., Paris Saint-Germain, Stade Brestois, OGC Nice...",
    )
    
with col2:
    api_key_input = st.text_input(
        "ADVISORY ACCESS TOKEN :", 
        type="password", 
        placeholder="Enter credentials...",
        help="Required for dynamic generation."
    )

# Safely extract base64 logo for template embedding
logo_b64 = ""
if os.path.exists("logo_itbr.b64.txt"):
    with open("logo_itbr.b64.txt", "r") as f:
        logo_b64 = f.read().strip()
elif os.path.exists("logo_itbr.png"):
    with open("logo_itbr.png", "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode("utf-8")

# Elite M&A Corporate System Instructions with Strict Layout Rules
SYSTEM_INSTRUCTIONS = f"""
You are an elite, top-tier Sport Business M&A Analyst working for a major investment bank in London/New York. 
Your task is to generate a comprehensive, highly aesthetic, multi-slide investment memorandum HTML deck based on the requested sports asset.
The language of the deck MUST be strictly professional, corporate English.

CRITICAL VISUAL LAYOUT & LOGO CONSTRAINTS:
- Return ONLY valid HTML code starting with `<!DOCTYPE html>` and ending with `</html>`. No markdown wrapper (do NOT use ```html), no conversational chat.
- Every single slide must be enclosed in its own `<div class="slide-container">` block.
- Layout Dimensions per slide: exactly 1280px wide by 720px high. 
- Slide Background is pure white (`#ffffff`). Use deep navy headers (`#0F172A`) and electric blue accents (`#2563EB`).
- **LOGO REQUIREMENT**: Every single slide footer MUST display the official logo image in the bottom-left corner using the provided base64 string.
  HTML structure for the footer:
  <div class="footer">
      <div class="logo-area"><img src="data:image/png;base64,{logo_b64}" style="height:35px; max-width:180px; object-fit:contain;"/></div>
      <div class="confidentiality-notice">STRICTLY CONFIDENTIAL - WORK MATERIAL</div>
      <div class="page-number">Slide [X]</div>
  </div>

DECK STRUCTURE:
- Slide 1: Premium Strategic Title Slide (Asset Name, Valuation Context, Date).
- Slide 2: Market Landscape & Commercial Revenues (Media rights, global sponsorships, commercial expansion vectors).
- Slide 3: M&A Valuation Analytics & Comparables (Provide precise revenue multiples, EV indications, and transaction benchmarks).
- Slide 4: Strategic Growth Roadmap & Investment Thesis (Infrastructure, internationalization, global digital footprint scaling).

DATA INTEGRITY:
Utilize your deep institutional knowledge of sports business, financial valuation metrics, and market data to make the deck exceptionally customized, sharp, and realistic for the target asset. Do not use generic text.
"""

# Professional Fallback Template
CLEAN_ENG_TEMPLATE = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="[https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700&display=swap](https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700&display=swap)" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ background-color: #0B0F19; display: flex; flex-direction: column; align-items: center; gap: 40px; padding: 40px; }}
        .slide-container {{
            width: 1280px; height: 720px; background: #ffffff; border-radius: 4px;
            padding: 50px 60px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden;
            font-family: 'Inter', sans-serif; color: #0F172A; margin-bottom: 30px;
        }}
        .slide-container::before {{ content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 6px; background-color: #2563EB; }}
        .header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #F1F5F9; padding-bottom: 15px; }}
        .slide-title {{ font-family: 'Poppins', sans-serif; font-size: 32px; color: #0F172A; }}
        .content {{ display: flex; flex-direction: column; justify-content: center; align-items: center; flex-grow: 1; text-align: center; }}
        .footer {{ display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: #94A3B8; border-top: 1px solid #F1F5F9; padding-top: 15px; }}
    </style>
</head>
<body>
<div class="slide-container">
    <div class="header"><div class="slide-title">STRATEGIC PROFILE INITIALIZED</div></div>
    <div class="content">
        <h1 style="font-family:'Poppins'; font-size:56px; color:#0F172A; margin-bottom:15px;">{subject.upper() if subject else "TARGET ASSET"}</h1>
        <div style="width:50px; height:4px; background:#2563EB; margin-bottom:20px;"></div>
        <p style="font-size:16px; color:#64748B; max-width:600px;">System synchronized. Click the generation trigger to compile the full multi-slide financial dossier via Claude 3.5 Sonnet.</p>
    </div>
    <div class="footer">
        <div><img src="data:image/png;base64,{logo_b64}" style="height:35px;"/></div>
        <div style="font-weight:600; letter-spacing:1px;">STRICTLY CONFIDENTIAL</div>
        <div>Slide 1</div>
    </div>
</div>
</body>
</html>
"""

if st.button("🚀 GENERATE INVESTMENT MEMORANDUM DECK"):
    target_asset = subject.strip() if subject.strip() else "Selected Sports Property"
    
    with st.spinner("Compiling institutional market data and rendering executive slides..."):
        final_api_key = api_key_input.strip() if api_key_input.strip() else st.secrets.get("ANTHROPIC_API_KEY")
        
        if final_api_key:
            try:
                client = Anthropic(api_key=final_api_key)
                prompt_payload = f"Compile a complete corporate M&A deck with detailed slides for {target_asset}. Build analytical charts, detailed market tables, and place the embedded logo correctly in the footer area."
                
                message = client.messages.create(
                    model="claude-3-5-sonnet-latest",
                    max_tokens=4000,
                    system=SYSTEM_INSTRUCTIONS,
                    messages=[{"role": "user", "content": prompt_payload}]
                )
                html_result = message.content[0].text
            except Exception as e:
                st.error(f"Execution Error: {e}")
                html_result = CLEAN_ENG_TEMPLATE
        else:
            html_result = CLEAN_ENG_TEMPLATE

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
<div class="footer" style="text-align: center; margin-top: 50px;">
    <p>In The Boardroom • Institutional Platform © 2026</p>
</div>
""", unsafe_allow_html=True)