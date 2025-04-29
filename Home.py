import streamlit as st

# --- Titre principal ---
st.title("🌍 Valorisation des Circuits Courts")

# --- Slogan central ---
st.markdown(
    """
    ## Consommer local, c'est agir global ! 
    *Chaque achat est une action pour demain.*
    """,
    unsafe_allow_html=True
)

st.divider()

# --- Introduction rapide ---
st.write(
    """
    Bienvenue sur notre WebApp dédiée aux circuits courts 🌱.  
    Découvrez pourquoi consommer local est essentiel pour préserver l'environnement, soutenir l'économie locale et savourer des produits de qualité.  
    Explorez, apprenez et agissez à travers notre expérience interactive !
    """
)

st.divider()

# --- Vidéo à intégrer ---
st.subheader("🎥 Découvrez notre message en vidéo")

# Charge une vidéo locale
video_file = open('assets\sensibilisation_3.mp4', 'rb') 
video_bytes = video_file.read()

st.video(video_bytes)

# --- Bouton pour passer au quiz ---
st.divider()
if st.button("👉 Commencer le Quiz !"):
    st.switch_page("pages/Quiz.py")  # ATTENTION: nécessite Streamlit >= 1.20 et structure MultiPage si activée
