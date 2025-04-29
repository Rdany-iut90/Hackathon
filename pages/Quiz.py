import streamlit as st
import random

# Base de données des questions
questions_bank = [
    {
        "question": "Qu’est-ce qu’un circuit court ?",
        "options": [
            "Un produit vendu uniquement sur Internet",
            "Un mode de transport rapide des aliments",
            "Une vente avec zéro intermédiaire",
            "Une vente directe ou avec un seul intermédiaire"
        ],
        "answer": 3
    },
    {
        "question": "Quel est le principal avantage écologique des circuits courts ?",
        "options": [
            "Plus de publicité locale",
            "Moins de transport, donc moins d’émissions CO2",
            "Des produits emballés sous vide",
            "Une meilleure connexion Wi-Fi"
        ],
        "answer": 1
    },
    {
        "question": "Quelle structure permet d’acheter des paniers de producteurs locaux ?",
        "options": [
            "Supermarché solidaire",
            "AMAP",
            "Banque alimentaire",
            "FAST&FARM"
        ],
        "answer": 1
    },
    {
        "question": "Quel obstacle freine souvent l’adoption des circuits courts ?",
        "options": [
            "Trop d’options disponibles",
            "L’odeur des produits",
            "Le manque d’accessibilité ou d’information",
            "L’absence de carte bancaire"
        ],
        "answer": 2
    },
    {
        "question": "Quel slogan pourrait promouvoir les circuits courts ?",
        "options": [
            "Moins d’intermédiaires, plus de fraîcheur !",
            "Toujours plus, toujours plus loin !",
            "Mange vite, mange loin.",
            "Importons la planète."
        ],
        "answer": 0
    },
    {
        "question": "Quelle plateforme facilite l’achat direct à des producteurs locaux ?",
        "options": [
            "La Ruche Qui Dit Oui",
            "Uber Eats",
            "Deliveroo",
            "Goût Express"
        ],
        "answer": 0
    },
    {
        "question": "Que permet une production locale et de saison ?",
        "options": [
            "De manger des fraises toute l’année",
            "De soutenir l’économie chinoise",
            "D’optimiser la qualité gustative et nutritionnelle",
            "D’importer plus de bananes"
        ],
        "answer": 2
    },
    {
        "question": "Quel est le gain potentiel pour un producteur en circuit court ?",
        "options": [
            "Un revenu plus élevé",
            "Une assurance gratuite",
            "Moins de clients",
            "Une réduction fiscale automatique"
        ],
        "answer": 0
    },
    {
        "question": "En France, quel pourcentage approximatif des exploitations vend en circuits courts ?",
        "options": [
            "5%",
            "10%",
            "21%",
            "50%"
        ],
        "answer": 2
    },
    {
        "question": "Quel est un effet positif sur la biodiversité ?",
        "options": [
            "Plus d’engrais chimiques",
            "Favorise la monoculture",
            "Moins de diversité de fruits",
            "Encouragement à des pratiques agricoles durables"
        ],
        "answer": 3
    }
]

# INITIALISATION SESSION STATE
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = random.sample(questions_bank, 10)
if "user_answers" not in st.session_state:
    st.session_state.user_answers = [None] * 10
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False
if "show_answers" not in st.session_state:
    st.session_state.show_answers = False

# Affichage du Quiz
st.title("Quiz Circuits Courts")
st.write("Testez vos connaissances sur l'impact des circuits courts !")

for idx, question in enumerate(st.session_state.selected_questions):
    st.subheader(f"Question {idx + 1}")

    if st.session_state.user_answers[idx] is not None:
        default_index = st.session_state.user_answers[idx]
    else:
        default_index = 0

    user_choice = st.radio(
        question['question'],
        question['options'],
        index=default_index,
        key=f"question_{idx}"
    )
    st.session_state.user_answers[idx] = question['options'].index(user_choice)

# Vérification des réponses
if st.button("Valider mes réponses"):
    score = 0
    for i, question in enumerate(st.session_state.selected_questions):
        if st.session_state.user_answers[i] == question['answer']:
            score += 1

    st.success(f"Votre score final est de {score}/10")

    # Message simple selon score
    if score >= 8:
        st.info("🏆 Excellent ! Vous êtes un ambassadeur des circuits courts !")
        st.markdown("""
        **Message personnalisé pour vous :**  
        Bravo pour votre implication ! 🌱 Vous connaissez déjà bien les circuits courts et leur importance écologique.  
        ➔ Continuez à privilégier les producteurs locaux.  
        ➔ Parlez-en autour de vous pour inspirer vos proches !  
        ➔ Pourquoi ne pas rejoindre une AMAP ou soutenir un marché local ?
        """)
    elif score >= 5:
        st.info("👍 Bon début ! Continuez à vous informer pour devenir un acteur local.")
        st.markdown("""
        **Message personnalisé pour vous :**  
        Vous êtes sur la bonne voie pour consommer de manière plus responsable.  
        ➔ Essayez d'acheter 1 produit local par semaine pour commencer.  
        ➔ Renseignez-vous sur les saisons des fruits et légumes.  
        ➔ Visitez un marché de producteurs ce mois-ci !
        """)
    else:
        st.warning("🌱 Chaque effort compte, continuez à apprendre pour la planète !")
        st.markdown("""
        **Message personnalisé pour vous :**  
        Il est temps de découvrir l'impact réel de vos choix de consommation.  
        ➔ Privilégiez les achats locaux quand vous le pouvez.  
        ➔ Informez-vous sur les circuits courts dans votre région.  
        ➔ Un petit pas : choisissez un légume ou fruit de saison la prochaine fois !
        """)

    # score = 0
    # for i, question in enumerate(st.session_state.selected_questions):
    #     if st.session_state.user_answers[i] == question['answer']:
    #         score += 1

    # st.success(f"Votre score final est de {score}/10")

    # if score >= 8:
    #     st.info("Excellent ! Vous êtes un ambassadeur des circuits courts !")
    # elif score >= 5:
    #     st.info("Bon début ! Continuez à vous informer pour devenir un acteur local.")
    # else:
    #     st.warning("Chaque effort compte, continuez à apprendre pour la planète !")

    st.session_state.quiz_completed = True

# Si le quiz est terminé, proposer deux boutons côte à côte
if st.session_state.quiz_completed:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Rejouer le quiz"):
            del st.session_state.selected_questions
            del st.session_state.user_answers
            st.session_state.quiz_completed = False
            st.session_state.show_answers = False
            st.rerun()

    with col2:
        if st.button("Afficher les réponses"):
            st.session_state.show_answers = True

# Affichage des réponses correctes
if st.session_state.show_answers:
    st.header("Réponses correctes")
    for idx, question in enumerate(st.session_state.selected_questions):
        st.write(f"**Q{idx + 1} : {question['question']}**")
        for i, option in enumerate(question['options']):
            if i == question['answer']:
                st.markdown(f"- ✅ **{option}**", unsafe_allow_html=True)
            else:
                st.markdown(f"- {option}")
        st.write("---")