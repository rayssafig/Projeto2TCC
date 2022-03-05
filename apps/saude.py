# %%writefile app.py
import streamlit as st
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

os.add_dll_directory('C:/Users/rayss/anaconda3/DLLs')

# countries = 'C:/Users/rayss/PycharmProject/TCC/countries.geojson'
countries = gpd.read_file('C:/Users/rayss/PycharmProject/TCC/countries.geojson')
print(countries)

st.header(f'Mapa de casos por bairro')
m = folium.Map(location=[-25.5, -49.3], tiles='Stamen Terrain', zoom_start=11)

folium.LayerControl().add_to(m)
folium_static(m)
