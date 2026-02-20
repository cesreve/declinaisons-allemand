import streamlit as st

st.set_page_config(
    page_title="Apprentissage de l'allemand",
    page_icon="🇩🇪",
)

st.title("Bienvenue sur l'application d'apprentissage de l'allemand !")

st.sidebar.success("Sélectionnez une page ci-dessus.")

st.markdown(
    """
    Cette application est conçue pour vous aider à apprendre les déclinaisons allemandes.
    
    **👈 Sélectionnez une page dans la barre latérale** pour commencer !
    
    ### Pages disponibles:
    - **Leçon**: Pour apprendre les règles de déclinaison.
    - **Pratique**: Pour vous exercer avec des phrases à trous.
    """
)
