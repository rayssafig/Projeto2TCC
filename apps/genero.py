import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import codecs


def app():
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-05.png')
    titl.title('ODS 5: Igualdade de Gênero')
    st.subheader('Alcançar a igualdade de gênero e empoderar todas as mulheres e meninas')

    #a = pd.read_html('://labgeolivre@solimoes.ufpr.br/html/AtlasODSGenero/Meta54/Meta54.html')
    #b = pd.read_json(': // labgeolivre @ solimoes.ufpr.br / html / AtlasODSGenero / Meta54 / package - lock.json')

    st.image('http://moontrek.jpl.nasa.gov/trektiles/Moon/EQ/LRO_WAC_Mosaic_Global_303ppd_v02/1.0.0/default/default028mm/0/0/0.jpg')

    import urllib

    page = urllib.request.urlopen("http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html").read()
    #st.write(page)

    page = urllib.request.urlopen("http://www.labgeolivre.ufpr.br/AtlasODSGenero/Meta51/Meta51.html").read()
    st.write(page)


