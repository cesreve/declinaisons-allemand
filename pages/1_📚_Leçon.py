import streamlit as st

@st.cache_data
def load_lecon():
    with open("data/lecon.md", "r") as f:
        lecon = f.read()
    return lecon

lecon = load_lecon()

st.title("Leçon sur les déclinaisons allemandes")
st.markdown(lecon)
