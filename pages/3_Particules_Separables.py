import streamlit as st
import json
import random

st.set_page_config(
    page_title="Particules Séparables",
    page_icon="🇩🇪",
)

st.title("Les particules des verbes séparables")

with st.expander("Leçon"):
    st.markdown("""En allemand, de nombreux verbes sont formés avec une particule (un préfixe) qui peut se séparer du verbe principal. Cette particule modifie le sens du verbe.""")

    st.header("Qu'est-ce qu'un verbe à particule séparable ?")
    st.markdown("""Un verbe à particule séparable est un verbe dont le préfixe se détache et se place à la fin de la phrase conjuguée au présent ou au prétérit.

    *Exemple :* `anrufen` (appeler)
    > Ich **rufe** dich **an**. (Je t'appelle.)
    """)

    st.header("Liste des particules séparables courantes")
    st.markdown("""Voici une liste de particules séparables courantes avec leur signification générale et des exemples.""")
    st.markdown("""
    | Particule | Signification | Exemple | Traduction |
    | --- | --- | --- | --- |
    | **an-** | contact, début d'une action | `anrufen` | appeler |
    | **auf-** | ouverture, mouvement vers le haut | `aufstehen` | se lever |
    | **aus-** | sortie, extension | `ausgehen` | sortir |
    | **ein-** | entrée, introduction | `einkaufen` | faire les courses |
    | **mit-** | accompagnement | `mitkommen` | venir avec |
    | **nach-** | répétition, direction | `nachdenken` | réfléchir |
    | **vor-** | avant, présentation | `vorstellen` | présenter, imaginer |
    | **zu-** | fermeture, ajout | `zumachen` | fermer |
    """)

    st.header("Particules de sens contraire")
    st.markdown("""Certaines particules ont des significations opposées, ce qui peut aider à les mémoriser.""")
    st.markdown("""
    | Particule 1 | Signification 1 | Particule 2 | Signification 2 | Exemple |
    | --- | --- | --- | --- | --- |
    | **auf-** | ouverture | **zu-** | fermeture | `aufmachen` (ouvrir) / `zumachen` (fermer) |
    | **an-** | allumer | **aus-** | éteindre | `anmachen` (allumer) / `ausmachen` (éteindre) |
    | **ein-** | entrée | **aus-** | sortie | `einatmen` (inspirer) / `ausatmen` (expirer) |
    """)

with st.expander("Exercices"):
    st.cache_data.clear()
    # Charger les données
    def load_practice_data():
        with open("data/particules_separables_pratique.json", "r") as f:
            data = json.load(f)
        return data

    practice_data = load_practice_data()

    st.header("Mode Pratique")

    difficulty = st.radio("Choisissez un niveau de difficulté :", (1, 2, 3), index=0)

    if 'question_indices_particules' not in st.session_state or st.session_state.get('difficulty') != difficulty:
        st.session_state.question_indices_particules = list(range(len(practice_data)))
        random.shuffle(st.session_state.question_indices_particules)
        st.session_state.difficulty = difficulty

    def reset_session_particules():
        st.session_state.question_indices_particules = list(range(len(practice_data)))
        random.shuffle(st.session_state.question_indices_particules)
        if 'answered_particules' in st.session_state:
            del st.session_state['answered_particules']
        if 'user_answer_input_particules' in st.session_state:
            st.session_state.user_answer_input_particules = ""
        st.rerun()

    if not st.session_state.question_indices_particules:
        st.success("🎉 Bravo ! Vous avez terminé tous les exercices.")
        if st.button("Recommencer"):
            reset_session_particules()
        st.stop()

    def next_question_callback_particules():
        st.session_state.answered_particules = False
        st.session_state.user_answer_input_particules = ""
        st.session_state.question_indices_particules.pop(0)

    def verify_answer_callback_particules():
        st.session_state.answered_particules = True

    current_question_index = st.session_state.question_indices_particules[0]
    exercise = practice_data[current_question_index]
    
    phrase_to_display = exercise["phrase"]
    if difficulty == 1:
        phrase_to_display += exercise["verbe"]
    elif difficulty == 2:
        phrase_to_display += exercise["base_verbe"]

    # Afficher l'exercice
    st.markdown(f'<h3>{phrase_to_display}</h3>', unsafe_allow_html=True)
    st.markdown(f"<i>{exercise['traduction']}</i>", unsafe_allow_html=True)


    # Champ de réponse
    user_answer = st.text_input("Votre réponse", key="user_answer_input_particules")

    st.button("Vérifier", on_click=verify_answer_callback_particules)

    if 'answered_particules' in st.session_state and st.session_state.answered_particules:
        if user_answer.lower() == exercise["reponse"].lower():
            st.balloons()
            st.success("Correct !")
        else:
            st.error(f'Incorrect. La bonne réponse est **{exercise["reponse"]}**.')
        
        st.button("Suivant", on_click=next_question_callback_particules)
