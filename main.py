import base64

import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs
from appart_a_louer import scrap_appart_a_louer
from appart_meuble import scrap_appart_meuble
from terrain_a_vendre import srappe_terrain_a_vendre


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

# Page Principale
st.title("Projet de Data Collection Groupe 5")
st.write(
    "This app performs webscraping of data from expat-dakar over multiples pages. "
    "And we can also download scraped data from the app directly without scraping them.")
st.markdown("- Python libraries: base64, pandas, streamlit, requests, bs4")
st.markdown("- Data source: at-Dakar.")

# Barre de Menu lattérale
st.sidebar.title("Menu")

# création d'une liste de 1 à 100
list1 = [i for i in range(1, 101)]

option1 = st.sidebar.selectbox(
    "Pages indexes",
    list1,
)

option2 = st.sidebar.selectbox(
    "Options",
    ("Scrape data using beautifulSoup", "Download scraped data", "Dashbord of the data", "Fill the form"),
    index=None
)


def load(dataframe, title, key, key1):
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title, key1):
        # st.header(title)

        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

        csv = dataframe.to_csv().encode('utf-8')

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Data.csv',
            mime='text/csv',
            key=key)


if option2 == "Scrape data using beautifulSoup":
    appart_a_louer = scrap_appart_a_louer(option1)
    appart_meuble = scrap_appart_meuble(option1)
    terrain_a_vendre = srappe_terrain_a_vendre(option1)

    load(appart_a_louer, 'Appartements à louer', '1', '101')
    load(appart_meuble, 'Appartement meublés', '2', '102')
    load(terrain_a_vendre, 'Terrains à vendre', '3', '103')

# load(Motocycles, 'Motocycles data', '2', '102')
# st.bar_chart(data=appart_louer, x=None, y=None, color=None, width=0, height=0, use_container_width=True)
