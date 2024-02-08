import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs
from menu import menu

st.title("Projet de Data Collection Groupe 5")
st.sidebar.title("Menu")

option1 = st.sidebar.selectbox(
    "Qu'est-ce vous voulez scrapper ?",
    ("Appartements à louer", "Meubles pour appartement", "Terrains à vendre"),
    index=None,
    placeholder="Sélectionner une option",
)

st.write('Vous avez sélectionné:', option1)

list1 = [i for i in range(1, 101)]
option2 = st.sidebar.selectbox(
    "Nombre de page à scrapper",
    list1,
    index=None,
    placeholder="Sélectionner une option",
)

st.write('Vous avez sélectionné:', option2)


def scrapper():
    pass
