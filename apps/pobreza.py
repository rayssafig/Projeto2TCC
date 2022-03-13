import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd


def app():

    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-01.png')
    titl.title('ODS 1: Erradicação da pobreza')
    st.subheader('Erradicar a pobreza em todas as formas e em todos os lugares')

    st.title('Mapas folium')
    st.subheader('Indicador 1.1.1: Proporção da população abaixo da linha de pobreza internacional (porcentagem)')
    st.write('A proporção da população que vive abaixo da linha de pobreza extrema caiu de 22,0% em 1990 para 4,0% em 2018.')

    poverty = gpd.read_file('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SI_POV_DAY1_1_1_1_2020Q2G03/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson')

    poverty1 = gpd.read_file('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SI_POV_DAY1_1_1_1_2020Q2G03/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

    m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Terrain', zoom_start=1.5)
    folium.Choropleth(
        geo_data=poverty,
        name='Casos por bairro',
        columns=['BAIRRO', 'CLASSIFICAÇÃO FINAL'],
        key_on='feature.properties.BAIRRO',
        fill_color='Reds',
        legend_name='Casos por bairro'
    ).add_to(m)
    folium.LayerControl().add_to(m)
    #mostrar folium map no streamlit
    folium_static(m)





































































































































































































































