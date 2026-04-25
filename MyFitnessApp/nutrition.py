# nutrition.py
import streamlit as st
from database import PLATS

def afficher_nutrition():
    st.title("🥗 Mon Programme Alimentaire")
    
    if 'mon_menu' not in st.session_state:
        st.session_state.mon_menu = []

    if st.button("🔄 Refresh le menu") or not st.session_state.mon_menu:
        import random
        # On sélectionne un de chaque pour l'exemple
        p_dej = random.choice([x for x in PLATS if x["type"] == "Petit-déj"])
        dej = random.choice([x for x in PLATS if x["type"] == "Déjeuner"])
        st.session_state.mon_menu = [p_dej, dej]

    # Affichage détaillé
    for item in st.session_state.mon_menu:
        with st.expander(f"📖 {item['nom']} - {item['cal']} kcal", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**📊 Macros :**")
                st.write(f"Protéines : {item['macros']['P']}g")
                st.write(f"Glucides : {item['macros']['G']}g")
                st.write(f"Lipides : {item['macros']['L']}g")
            
            with col2:
                st.write("**⚖️ Quantités :**")
                for ing, qte in item['portions'].items():
                    st.write(f"- {ing} : {qte}")
            
            st.write("**👨‍🍳 Recette :**")
            for etape in item['recette']:
                st.write(f". {etape}")