import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs
from menu import menu

# Page Principale
st.title("Projet de Data Collection Groupe 5")
st.write(
    "This app performs webscraping of data from expat-dakar over multiples pages. "
    "And we can also download scraped data from the app directly without scraping them.")
st.markdown("- Python libraries: base64, pandas, streamlit, requests, bs4")
st.markdown("- Data source: at-Dakar.")

# Barre de Menu lattérale
st.sidebar.title("User Input Features")

list1 = [i for i in range(1, 101)]
option1 = st.sidebar.selectbox(
    "Pages indexes",
    list1,
)

option2 = st.sidebar.selectbox(
    "Options",
    ("Scrape data using beautifulSoup", "Download scraped data", "Dashbord of the data", "Fill the form")
)

st.write('Vous avez sélectionné:', option1)
st.write('Vous avez sélectionné:', option2)

st.sidebar.button("Scraper les Data", type="primary", on_click='scraper_page', args=(option1, option2))


def scraper_page():
    """
    Fonction qui permet de scraper de les les pages avec BeautifulSoup
    :return: Pandas DataFrame
    """
    pass
