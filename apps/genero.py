import streamlit as st
import pandas as pd
import pandas
import geopandas as gpd
from streamlit_folium import folium_static
import folium


def app():
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-05.png')
    titl.title('ODS 5: Igualdade de Gênero')
    st.subheader('Alcançar a igualdade de gênero e empoderar todas as mulheres e meninas')

    a = pd.read_html('://labgeolivre@solimoes.ufpr.br/html/AtlasODSGenero/Meta54/Meta54.html')
    #b = pd.read_json(': // labgeolivre @ solimoes.ufpr.br / html / AtlasODSGenero / Meta54 / package - lock.json')

