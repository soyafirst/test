# app.py
import streamlit as st
# Importation de tes modules (fichiers séparés)
from nutrition import afficher_nutrition
from muscu import afficher_muscu
from courses import afficher_courses
from vision import scanner_plat  # Nouveau module IA

# 1. Configuration de la fenêtre (Centered est mieux pour le look téléphone)
st.set_page_config(page_title="My Fitness App", layout="centered", page_icon="🔥")

# 2. Style CSS (Le look Orange & Dark que tu aimes)
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: white; }
    [data-testid="stSidebar"] { background-color: #1E1E1E; border-right: 1px solid #333; }
    h1, h2, h3 { color: #FF5722 !important; font-weight: bold; }
    
    .stButton>button { 
        background-color: #FF5722; 
        color: white; 
        border-radius: 10px; 
        border: none;
        width: 100%;
        font-weight: bold;
        height: 3em;
    }
    .stButton>button:hover { background-color: #E64A19; color: white; }
    
    .meal-card, .train-card { 
        background: #262626; 
        padding: 20px; 
        border-radius: 15px; 
        border-left: 5px solid #FF5722;
        margin-bottom: 15px;
    }
    /* Style pour les métriques (Calories) */
    [data-testid="stMetricValue"] { color: #FF5722 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Menu latéral de navigation amélioré
st.sidebar.title("🛠️ COACH PERSO")
page = st.sidebar.radio(
    "Navigation", 
    ["🏠 Dashboard", "📸 Scanneur IA", "🏋️ Musculation", "🛒 Liste de Courses"]
)

# 4. Logique d'affichage des pages
if page == "🏠 Dashboard":
    afficher_nutrition()

elif page == "📸 Scanneur IA":
    scanner_plat()

elif page == "🏋️ Musculation":
    afficher_muscu()

elif page == "🛒 Liste de Courses":
    afficher_courses()

# Pied de page
st.sidebar.markdown("---")
st.sidebar.caption("Fitness App v1.0 • Ton IA de poche")