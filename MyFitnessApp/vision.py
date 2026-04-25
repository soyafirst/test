# vision.py
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Remplace par ta vraie clé obtenue sur Google AI Studio
genai.configure(api_key="AIzaSyDotZJrdx3h-H9Jgt2eqxDvYP3hbj02Spk")

def scanner_plat():
    st.title("📸 Scanneur IA")
    st.write("Prends une photo de ton plat pour analyser les calories.")

    img_file = st.camera_input("Scanner mon assiette")

    if img_file is not None:
        img = Image.open(img_file)
        st.image(img, caption="Analyse en cours...", width=300)
        
        with st.spinner("L'IA réfléchit..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = """
            Analyse cette photo de nourriture. 
            Donne-moi uniquement les informations suivantes sous ce format précis :
            Nom du plat : [Nom]
            Calories estimées : [Nombre] kcal
            Protéines : [Nombre]g
            Glucides : [Nombre]g
            Lipides : [Nombre]g
            Ingrédients identifiés : [Liste]
            """
            
            response = model.generate_content([prompt, img])
            
            st.markdown("### 🤖 Résultat de l'IA")
            st.info(response.text)
            
            if st.button("➕ Ajouter ce plat à ma base"):
                st.success("Plat mémorisé ! (Logique à connecter à database.py)")