import streamlit as st
import json
import random

st.set_page_config(
    page_title="Leçon sur le Perfekt",
    page_icon="🇩🇪",
)

st.title("Das Perfekt")

with st.expander("1. Das konjugierte HILFSVERB"):
    st.markdown("L'auxiliaire se place à la **2ème position** dans la phrase.")

    st.markdown("### A. haben")
    st.markdown("C'est l'auxiliaire utilisé dans la **plupart des cas**.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        | Personne | Forme conjuguée |
        | :--- | :--- |
        | **ich** | habe |
        | **du** | hast |
        | **er/sie/es** | hat |
        | **wir** | haben |
        | **ihr** | habt |
        | **sie/Sie** | haben |
        """)

    st.markdown("### B. sein")
    st.markdown("""
    Utilisé dans les cas suivants :

    * **Changement de lieu (Ortsveränderung) :**
        * Exemples : fahren, gehen, fliegen, reisen, schwimmen, wandern...
    * **Changement d'état (neuer Zustand) :**
        * Exemples : einschlafen, aufwachen.
    * **Verbes spécifiques :**
        * werden, sein, bleiben, gelingen, misslingen, geschehen, passieren.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        | Personne | Forme conjuguée |
        | :--- | :--- |
        | **ich** | bin |
        | **du** | bist |
        | **er/sie/es** | ist |
        | **wir** | sind |
        | **ihr** | seid |
        | **sie/Sie** | sind |
        """)

with st.expander("2. Infinite Verbform: PARTIZIP II"):
    st.markdown("Le participe II se place toujours **à la fin de la phrase**.")

    st.markdown("### 1. Regelmäßige Verben (Verbes réguliers)")

    st.markdown("""
    * **Règle générale (\"normale\") :**
        * **ge + ......... + t**
        * machen -> gemacht
        * kochen -> gekocht
    """)
    st.markdown("""*Ex :* Ich <span style='color:red'>habe</span> die Hausaufgabe <span style='color:blue'>gemacht</span>.""", unsafe_allow_html=True)


    st.markdown("""
    * **Verbes se terminant par -t, -d, -ffn, -tm, -chn, -dn, -gn :**
        * **ge + ......... + et**
        * warten -> gewartet
        * baden -> gebadet
    """)
    st.markdown("""*Ex :* Er <span style='color:red'>hat</span> gestern lange <span style='color:blue'>gearbeitet</span>.""", unsafe_allow_html=True)

    st.markdown("""
    * **Verbes avec la terminaison -ieren :**
        * **......... + t** (pas de préfixe "ge-")
        * studieren -> studiert
        * telefonieren -> telefoniert
    """)
    st.markdown("""*Ex :* Meine Schwester <span style='color:red'>hat</span> Medizin <span style='color:blue'>studiert</span>.""", unsafe_allow_html=True)

    st.markdown("""
    * **Verbes à particule séparable :**
        * Particules : aus-, an-, ab-, auf-, bei-, ein-, fern-, heim-, hin-, her-, mit-, nach-, statt-, weg-, zu-, zurück-.
        * **... + ge + ......... + t**
        * aufwachen -> aufgewacht
        * einkaufen -> eingekauft
    """)
    st.markdown("""*Ex :* Max <span style='color:red'>ist</span> heute sehr spät <span style='color:blue'>aufgewacht</span>.""", unsafe_allow_html=True)


    st.markdown("""
    * **Verbes à particule inséparable :**
        * Particules : miss-, be-, ge-, er-, ver-, zer-, emp-, ent-.
        * **......... + t** (pas de préfixe "ge-")
        * besuchen -> besucht
        * verkaufen -> verkauft
    """)
    st.markdown("""*Ex :* Wann <span style='color:red'>hast</span> du das Auto <span style='color:blue'>verkauft</span>?""", unsafe_allow_html=True)


    st.markdown("### 2. Unregelmäßige Verben (Verbes irréguliers)")
    st.markdown("""
    * Se référer au tableau spécifique (**TABELLE**).
    """)

with st.expander("3. Beispieltext"):
    st.markdown("""
    Gestern **habe** ich meine Freunde **besucht**. Wir **sind** ins Kino **gegangen** und **haben** einen lustigen Film **gesehen**. Nach dem Kino **haben** wir in einem Restaurant **gegessen**. Ich **habe** eine Pizza **bestellt** und meine Freunde **haben** Pasta **gegessen**. Wir **haben** viel **geredet** and **gelacht**. Es **ist** ein schöner Abend **gewesen**.
    """)
    st.markdown("""
    <i style="font-size:small;">
    Hier, j'ai rendu visite à mes amis. Nous sommes allés au cinéma et avons vu un film amusant. Après le cinéma, nous avons mangé dans un restaurant. J'ai commandé une pizza et mes amis ont mangé des pâtes. Nous avons beaucoup parlé et ri. C'était une belle soirée.
    </i>
    """, unsafe_allow_html=True)

with st.expander("4. Exercices"):
    # Charger les données
    @st.cache_data
    def load_practice_data():
        with open("data/perfekt_pratique.json", "r") as f:
            data = json.load(f)
        return data

    practice_data = load_practice_data()

    st.header("Mode Pratique")

    # recuperer toutes les categories
    all_categories = list(set([ex["category"] for ex in practice_data]))
    selected_categories = st.multiselect("Choisissez une ou plusieurs catégories de verbes :", all_categories)

    # Filtrer les exercices en fonction du cas sélectionné
    if selected_categories:
        filtered_practice_data = [ex for ex in practice_data if ex["category"] in selected_categories]
    else:
        filtered_practice_data = practice_data


    # Fonctions pour gérer l'état
    def next_question_callback():
        st.session_state.next_question_flag = True

    def verify_answer_callback():
        st.session_state.answered = True

    # Initialiser l'état de la session
    if "exercise_perfekt" not in st.session_state or st.session_state.get("selected_categories") != selected_categories:
        st.session_state.exercise_perfekt = random.choice(filtered_practice_data)
        st.session_state.answered = False
        st.session_state.user_answer_input = ""
        st.session_state.next_question_flag = False
        st.session_state.selected_categories = selected_categories

    # Gérer le passage à la question suivante
    if st.session_state.get("next_question_flag", False):
        st.session_state.exercise_perfekt = random.choice(filtered_practice_data)
        st.session_state.answered = False
        st.session_state.user_answer_input = ""
        st.session_state.next_question_flag = False


    exercise = st.session_state.exercise_perfekt

    # Afficher l'exercice
    st.markdown(f'<h3>{exercise["phrase"]}</h3>', unsafe_allow_html=True)

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
