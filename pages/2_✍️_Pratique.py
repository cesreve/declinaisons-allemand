import streamlit as st
import json
import random

# Charger les données
@st.cache_data
def load_practice_data():
    with open("data/pratique.json", "r") as f:
        data = json.load(f)
    return data

practice_data = load_practice_data()

st.header("Mode Pratique")

# Menu déroulant pour sélectionner le cas
all_cases = ["Tous"] + list(set([ex["cas"] for ex in practice_data]))
selected_case = st.selectbox("Choisissez un cas à pratiquer :", all_cases)

# Filtrer les exercices en fonction du cas sélectionné
if selected_case == "Tous":
    filtered_practice_data = practice_data
else:
    filtered_practice_data = [ex for ex in practice_data if ex["cas"] == selected_case]

# Fonctions pour gérer l\"état
def next_question_callback():
    st.session_state.next_question_flag = True

def verify_answer_callback():
    st.session_state.answered = True

# Initialiser l\"état de la session
if "exercise" not in st.session_state or st.session_state.get("selected_case") != selected_case:
    st.session_state.exercise = random.choice(filtered_practice_data)
    st.session_state.answered = False
    st.session_state.user_answer_input = ""
    st.session_state.next_question_flag = False
    st.session_state.selected_case = selected_case

# Gérer le passage à la question suivante
if st.session_state.get("next_question_flag", False):
    st.session_state.exercise = random.choice(filtered_practice_data)
    st.session_state.answered = False
    st.session_state.user_answer_input = ""
    st.session_state.next_question_flag = False


exercise = st.session_state.exercise

# Définir la couleur en fonction du genre
color_map = {
    "Maskulin": "blue",
    "Feminin": "pink",
    "Neutrum": "green",
    "Pluriel": "purple"
}
color = color_map.get(exercise["genre"], "black")

# Afficher l\"exercice avec la couleur
st.markdown(f'<h3 style="color:{color};">{exercise["phrase"]}</h3>', unsafe_allow_html=True)
st.markdown(f"<i>{exercise['traduction']}</i>", unsafe_allow_html=True)


# Champ de réponse
user_answer = st.text_input("Votre réponse", key="user_answer_input")

st.button("Vérifier", on_click=verify_answer_callback)

if st.session_state.answered:
    if user_answer.lower() == exercise["reponse"].lower():
        st.balloons()
        st.success("Correct !")
    else:
        st.error(f'Incorrect. La bonne réponse est **{exercise["reponse"]}**.')
        st.info(f'**Règle :** {exercise["regle"]}')
    
    st.button("Suivant", on_click=next_question_callback)
