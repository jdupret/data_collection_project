import base64

import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs

# Page Principale
st.title("Projet de Data Collection Groupe 5")
st.write(
    "This app performs webscraping of data from expat-dakar over multiples pages. "
    "And we can also download scraped data from the app directly without scraping them.")
st.markdown("- Python libraries: base64, pandas, streamlit, requests, bs4")
st.markdown("- Data source: at-Dakar.")

# Barre de Menu lattérale
st.sidebar.title("User Input Features")

# création d'une liste de 1 à 100
list1 = [i for i in range(1, 101)]

option1 = st.sidebar.selectbox(
    "Pages indexes",
    list1,
)

option2 = st.sidebar.selectbox(
    "Options",
    ("Scrape data using beautifulSoup", "Download scraped data", "Dashbord of the data", "Fill the form")
)

appart_a_louer = pd.read_csv('expat_dakar_appart_alouer.csv')
appart_meuble = pd.read_csv('expat_dakar_appart_meuble.csv')
terrain_a_vendre = pd.read_csv('expat_dakar_terrain_a_vendre.csv')


# st.bar_chart(data=appart_louer, x=None, y=None, color=None, width=0, height=0, use_container_width=True)

# Fonction Background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('background.jpg')


def scraper_page():
    """
    Fonction qui permet de scraper de les les pages avec BeautifulSoup
    :return: Pandas DataFrame
    """
