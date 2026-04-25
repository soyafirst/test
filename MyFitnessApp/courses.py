# courses.py
import streamlit as st

def afficher_courses():
    st.title("🛒 Ma Liste de Courses")
    st.write("Basée sur tes repas sélectionnés dans le Dashboard.")

    # On vérifie si l'utilisateur a choisi des plats dans la session
    if 'mon_menu' in st.session_state and st.session_state.mon_menu:
        
        # On crée un dictionnaire pour regrouper les ingrédients
        liste_finale = {}

        for plat in st.session_state.mon_menu:
            for ingredient, quantite in plat['portions'].items():
                # Si l'ingrédient est déjà dans la liste, on pourrait l'additionner 
                # (plus complexe à cause des unités g/ml, donc on les liste simplement pour l'instant)
                if ingredient not in liste_finale:
                    liste_finale[ingredient] = [quantite]
                else:
                    liste_finale[ingredient].append(quantite)

        st.markdown("---")
        
        # Affichage avec des cases à cocher pour ton shopping
        for ing, qtes in liste_finale.items():
            # On affiche l'ingrédient et la somme des quantités
            affichage_qte = " + ".join(qtes)
            st.checkbox(f"**{ing}** : {affichage_qte}")

        st.markdown("---")
        if st.button("🗑️ Vider la liste"):
            st.session_state.mon_menu = []
            st.rerun()
            
    else:
        st.warning("⚠️ Ta liste est vide. Va sur le Dashboard et génère un menu !")
        st.info("L'app lira automatiquement les ingrédients des plats affichés là-bas.")