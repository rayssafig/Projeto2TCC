# %%writefile app.py
import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
import geopandas
import geopandas as gpd
import os
import pandas
import plotly.express as px
import fiona
import matplotlib.pyplot as plt
import io
import requests
import openpyxl
import fiona
user_input = st.container()
output_graphs = st.container()
def app():

    st.title("Saude")

url = "https://unstats.un.org/SDGAPI/v1/sdg/Indicator/List"
df = pd.read_json(url)


#os.add_dll_directory('C:/Users/rayss/anaconda3/DLLs')

# countries = 'C:/Users/rayss/PycharmProject/TCC/countries.geojson'
#countries = gpd.read_file(os.path.normpath('C:/Users/rayss/PycharmProject/Projeto2TCC/bairros_novo.geojson'))
print("teste")

#st.header(f'Mapa de casos por bairro')
#m = folium.Map(location=[-25.5, -49.3], tiles='Stamen Terrain', zoom_start=11)

#folium.LayerControl().add_to(m)
#folium_static(m)


