# muscu.py
import streamlit as st
import pandas as pd
from datetime import datetime
from database import MACHINES

def afficher_muscu():
    st.title("🏋️ Mon Traqueur de Charges")
    
    # --- 1. Formulaire d'ajout ---
    st.subheader("➕ Noter une série")
    with st.container():
        # On utilise une "card" pour le style
        st.markdown("<div class='train-card'>", unsafe_allow_html=True)
        
        col_exo, col_pds, col_reps = st.columns([2, 1, 1])
        
        with col_exo:
            exercice = st.selectbox("Machine / Exercice", MACHINES)
        with col_pds:
            poids = st.number_input("Poids (kg)", min_value=0.0, step=0.5)
        with col_reps:
            reps = st.number_input("Reps", min_value=0, step=1)
            
        if st.button("✅ Valider la série"):
            nouvelle_data = {
                "Date": datetime.now().strftime("%d/%m/%Y"),
                "Exercice": exercice,
                "Poids": poids,
                "Reps": reps
            }
            sauvegarder_perf(nouvelle_data)
            st.success("Série enregistrée !")
        
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    # --- 2. Affichage de l'historique ---
    st.subheader("📈 Historique des records")
    afficher_historique()

def sauvegarder_perf(data):
    # On utilise un fichier CSV pour stocker tes données sur ton PC
    try:
        df = pd.read_csv("stats_muscu.csv")
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([data])
    
    df.to_csv("stats_muscu.csv", index=False)

def afficher_historique():
    try:
        df = pd.read_csv("stats_muscu.csv")
        # On affiche les 10 dernières entrées, la plus récente en haut
        st.dataframe(df.iloc[::-1].head(10), use_container_width=True)
    except FileNotFoundError:
        st.info("Aucune séance enregistrée pour le moment. À toi de jouer !")