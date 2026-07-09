import streamlit as st
import streamlit.components.v1 as components
from anthropic import Anthropic
import os

# Configuration visuelle de la page
st.set_page_config(
    page_title="In The Boardroom - Factory v3.0",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS pour donner un look d'outil M&A ultra-premium
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }
    .stButton>button {
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        padding: 0.6rem 2rem !important;
        border: none !important;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1D4ED8 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
    }
    div[data-testid="stSidebarCollapseButton"] {
        display: none;
    }
    .reportview-container .main .footer {
        text-align: center;
        color: #64748B;
        font-size: 12px;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# Barre latérale - Configuration de sécurité
st.sidebar.image("https://images.stockcake.com/public/f/e/4/fe4c4fe9-4387-459c-a1d8-3c9ae4097615_medium/market-data-waves-stockcake.jpg", use_column_width=True)
st.sidebar.title("🛠️ Boardroom Engine")
api_key_input = st.sidebar.text_input(
    "Clé API Anthropic (Claude) :", 
    type="password", 
    placeholder="sk-ant-...",
    help="Insérez votre clé API pour activer la génération dynamique pour n'importe quel club."
)

st.sidebar.markdown("""
---
### 🛡️ Règles d'Intégrité de l'Agent
L'agent fonctionne sous un sandbox strict défini dans `CLAUDE.md` :
* **Zéro hallucination** de données M&A.
* **Bannissement absolu** de contenus créatifs ou poétiques.
* **Respect strict** de l'identité visuelle de la charte *intheboardroom*.
""")

# Titre Principal
st.title("🏆 In The Boardroom - Factory")
st.subheader("Générateur Automatique de Mémos Stratégiques & Slide Decks")
st.write("Entrez simplement le nom d'un club, d'une ligue ou d'un actif sportif pour générer un deck de slides HTML interactif, respectant parfaitement nos standards de conception.")

# Formulaire principal
col1, col2 = st.columns([2, 1])

with col1:
    subject = st.text_input(
        "Nom du Club, de la Ligue ou du Sujet :",
        placeholder="Ex: Stade Brestois 29, Ligue 1, Euroleague Basketball...",
    )
    focus = st.multiselect(
        "Focalisation des analyses (Optionnel) :",
        ["Droits TV & Audiences", "Profil des Participants & Démographie", "Valorisation & Opportunités M&A", "Roadmap Stratégique"],
        default=["Droits TV & Audiences", "Valorisation & Opportunités M&A"]
    )

with col2:
    st.write("💡 **Mode Démonstration Rapide**")
    demo_mode = st.checkbox("Activer le Mode Démo (Sans Clé API)", value=True, help="Permet de générer instantanément le deck validé du Stade Brestois sans utiliser de crédits d'API.")

# Template du prompt d'ingénierie système pour Claude
SYSTEM_INSTRUCTIONS = """
You are an elite Sport Business M&A Analyst. 
Generate a comprehensive, highly aesthetic, static HTML slide deck of exactly 4 slides based on the user's requested sports asset.
Each slide must be enclosed in its own `<div class="slide-container">` with dimensions of exactly `1280px` wide by `720px` high.

Visual Identity constraints (Consulting White Theme):
- Background: `#ffffff` with a subtle grid pattern or soft gradient.
- Colors: `#0F172A` (deep navy for headers), `#2563EB` (electric blue for accents), `#F8FAFC` (light grey cards), `#E2E8F0` (borders).
- Fonts: Poppins and Inter/Lato (imported via Google Fonts).
- Structure: Clear Title Slide, Structured Content Grid, Data Visualizations (clean CSS bar charts), and a Q&A / Contact Slide.
- Clean typography and perfect alignment of headers and text.

Data Integrity rule:
- DO NOT invent, guess, or extrapolate non-public financial metrics. If data is unknown, use "Vérification en cours (Data Room)" or label clearly as "Estimation indicative".
"""

# Simulation de données pour le Mode Démo (Stade Brestois 29)
DEMO_HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Stade Brestois 29 - Projet Iroise</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Poppins:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background-color: #f1f5f9; display: flex; flex-direction: column; align-items: center; gap: 20px; padding: 20px; }
        .slide-container {
            width: 1280px; height: 720px; background: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0;
            padding: 60px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05); font-family: 'Inter', sans-serif;
        }
        .slide-container::before {
            content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 6px; background-color: #2563EB;
        }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #f1f5f9; padding-bottom: 20px; }
        .brand { font-family: 'Poppins', sans-serif; font-size: 16px; font-weight: 700; color: #0F172A; }
        .brand b { color: #2563EB; }
        .slide-title { font-family: 'Poppins', sans-serif; font-size: 36px; color: #0F172A; margin-top: 20px; }
        .content { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 40px; flex-grow: 1; align-items: center; margin-top: 20px; }
        p { font-size: 16px; color: #4B5563; line-height: 1.6; }
        .card { background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 30px; border-radius: 6px; }
        .kpi-num { font-size: 40px; font-weight: 800; color: #2563EB; }
        .footer { display: flex; justify-content: space-between; font-size: 11px; color: #94A3B8; border-top: 1px solid #f1f5f9; padding-top: 20px; }
        .bar-chart { display: flex; flex-direction: column; gap: 15px; width: 100%; }
        .bar-row { display: flex; align-items: center; gap: 20px; }
        .bar-label { width: 180px; font-weight: 600; font-size: 14px; text-align: right; }
        .bar-track { flex-grow: 1; height: 30px; background: #E2E8F0; border-radius: 4px; overflow: hidden; }
        .bar-fill { height: 100%; background: #2563EB; display: flex; align-items: center; justify-content: flex-end; padding-right: 15px; color: white; font-weight: 700; font-size: 12px; }
    </style>
</head>
<body>

<div class="slide-container">
    <div class="header">
        <div class="brand">inthe<b>boardroom</b> / Advisory</div>
        <div style="font-size:12px; color:#64748B; font-weight:700;">PROJET IROISE // CONFIDENTIEL</div>
    </div>
    <div class="content" style="grid-template-columns: 1fr; text-align:center;">
        <div style="padding: 40px 0;">
            <p style="color:#2563EB; font-weight:700; letter-spacing:3px; text-transform:uppercase; margin-bottom:15px;">M&A Opportunity Profile</p>
            <h1 style="font-family:'Poppins'; font-size:56px; color:#0F172A;">STADE BRESTOIS 29</h1>
            <div style="width:80px; height:4px; background:#2563EB; margin:30px auto;"></div>
            <p style="font-size:20px; max-width:800px; margin: 0 auto;">Évaluation de la valorisation de l'actif et structuration de la cession majoritaire dans le cadre du Projet Iroise.</p>
        </div>
    </div>
    <div class="footer"><span>Advisory Work Material</span><span>Slide 1 / 4</span></div>
</div>

<div class="slide-container">
    <div class="header">
        <div class="brand">inthe<b>boardroom</b></div>
        <div style="font-size:12px; color:#64748B; font-weight:700;">PROJET IROISE</div>
    </div>
    <h2 class="slide-title">Synthèse de la Valorisation de l'Actif</h2>
    <div class="content">
        <div>
            <p style="margin-bottom:20px;">Le Stade Brestois 29 est entré dans une nouvelle dimension grâce à sa qualification historique en coupe d'Europe et la livraison imminente de son nouveau stade (Horizon 2027).</p>
            <div class="card">
                <h3 style="color:#0F172A; margin-bottom:10px;">Thèse d'Arbitrage</h3>
                <p style="font-size:14px; margin-bottom:0;">La valeur de l'actif repose sur la maîtrise des coûts opérationnels (capitaux propres stables) et la captation de nouvelles recettes d'hospitalités.</p>
            </div>
        </div>
        <div style="display:flex; flex-direction:column; gap:20px;">
            <div class="card" style="text-align:center;">
                <div class="kpi-num">€120M - €140M</div>
                <div style="font-size:12px; color:#64748B; font-weight:700; text-transform:uppercase; margin-top:5px;">Estimation Enterprise Value</div>
            </div>
            <div class="card" style="text-align:center;">
                <div class="kpi-num">15 000</div>
                <div style="font-size:12px; color:#64748B; font-weight:700; text-transform:uppercase; margin-top:5px;">Capacité Futur Stade (2027)</div>
            </div>
        </div>
    </div>
    <div class="footer"><span>Strictly Confidential // Stade Brestois 29</span><span>Slide 2 / 4</span></div>
</div>

<div class="slide-container">
    <div class="header">
        <div class="brand">inthe<b>boardroom</b></div>
        <div style="font-size:12px; color:#64748B; font-weight:700;">PROJET IROISE</div>
    </div>
    <h2 class="slide-title">Structure Répartie des Revenus (Est. 2026)</h2>
    <div class="content" style="grid-template-columns: 1fr;">
        <div class="bar-chart">
            <div class="bar-row">
                <div class="bar-label">Droits TV Nationaux</div>
                <div class="bar-track"><div class="bar-fill" style="width: 45%;">45%</div></div>
            </div>
            <div class="bar-row">
                <div class="bar-label">Revenus Billetterie & Jour de Match</div>
                <div class="bar-track"><div class="bar-fill" style="width: 25%;">25%</div></div>
            </div>
            <div class="bar-row">
                <div class="bar-label">Sponsoring & Partenariats</div>
                <div class="bar-track"><div class="bar-fill" style="width: 20%;">20%</div></div>
            </div>
            <div class="bar-row">
                <div class="bar-label">Merchandising & Divers</div>
                <div class="bar-track"><div class="bar-fill" style="width: 10%;">10%</div></div>
            </div>
        </div>
    </div>
    <div class="footer"><span>Finances & Insights // Source Interne</span><span>Slide 3 / 4</span></div>
</div>

<div class="slide-container">
    <div class="header">
        <div class="brand">inthe<b>boardroom</b></div>
        <div style="font-size:12px; color:#64748B; font-weight:700;">PROJET IROISE</div>
    </div>
    <div class="content" style="grid-template-columns: 1fr; text-align:center;">
        <div style="padding: 40px 0;">
            <h2 style="font-family:'Poppins'; font-size:48px; color:#0F172A; margin-bottom:15px;">Questions & Prochaines Étapes</h2>
            <p style="font-size:18px; max-width:600px; margin: 0 auto 40px;">Ce document sert de base exclusive aux discussions préliminaires menées par le bureau stratégique.</p>
            <div style="display:inline-block; border-top:1px solid #E2E8F0; padding-top:20px; font-size:14px; color:#2563EB; font-weight:700;">
                contact@intheboardroom.com | confidentiel-iroise@sb29.com
            </div>
        </div>
    </div>
    <div class="footer"><span>Strategic Briefing Concluded</span><span>Slide 4 / 4</span></div>
</div>

</body>
</html>
"""

# Logique de clic sur le bouton
if st.button("🚀 Générer le Slide Deck Stratégique"):
    if not demo_mode and not api_key_input.strip():
        st.error("❌ Veuillez coller votre clé API dans la barre latérale de gauche pour activer la génération dynamique.")
    elif not demo_mode and not subject.strip():
        st.warning("⚠️ Veuillez saisir le sujet ou nom de club requis pour la génération.")
    else:
        with st.spinner("L'agent analyse les dossiers et prépare l'assemblage graphique des slides..."):
            
            if demo_mode:
                # Mode Démo Instantané (Idéal pour impressionner le CEO directement)
                html_result = DEMO_HTML
                filename = "projet_iroise_sb29.html"
                st.success("✅ [MODE DÉMO ACTIVE] Deck stratégique du Stade Brestois 29 généré avec succès !")
            else:
                # Mode Production avec Appel API Claude 3.5 Sonnet
                try:
                    client = Anthropic(api_key=api_key_input.strip())
                    
                    prompt_payload = f"Generate a clean, professional M&A slide deck for {subject}. Include these focus areas: {', '.join(focus)}."
                    
                    message = client.messages.create(
                        model="claude-3-5-sonnet-20241022",
                        max_tokens=4000,
                        system=SYSTEM_INSTRUCTIONS,
                        messages=[{"role": "user", "content": prompt_payload}]
                    )
                    
                    html_result = message.content[0].text
                    filename = f"analyse_{subject.lower().replace(' ', '_')}.html"
                    st.success(f"✅ Analyse et slide deck générés dynamiquement avec succès pour {subject} !")
                except Exception as e:
                    st.error(f"❌ Une erreur est survenue lors de l'appel à l'agent : {e}")
                    html_result = None

            # Rendu et affichage du résultat
            if html_result:
                # Onglets pour voir le Rendu Interactif ou le Code Brut
                tab1, tab2 = st.tabs(["🖥️ Rendu Interactif (Preview)", "💻 Code HTML Brut"])
                
                with tab1:
                    st.write("💡 *Utilisez l'ascenseur de la zone ci-dessous pour faire défiler les slides à l'écran.*")
                    components.html(html_result, height=760, scrolling=True)
                
                with tab2:
                    st.code(html_result, language="html")
                
                # Bouton de téléchargement officiel du fichier HTML généré
                st.download_button(
                    label="📥 Télécharger le fichier HTML de présentation",
                    data=html_result,
                    file_name=filename,
                    mime="text/html"
                )

st.markdown("""
<div class="footer">
    <hr style="border-color:#E2E8F0;">
    <p>In The Boardroom Factory © 2026. Outil interne d'aide à la décision stratégique.</p>
</div>
""", unsafe_allow_html=True)