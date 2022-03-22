import streamlit as st
import geopandas as gpd
from streamlit_folium import folium_static
import folium


def app():
    global data
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-06.png')
    titl.title('ODS 6: Água potável e saneamento')
    st.subheader('Garantir a disponibilidade e a gestão sustentável da água potável e do saneamento para todos')

    # st.image('https://github.com/rayssafig/Projeto2TCC/tree/master/data/Irai_GIF.gif')
    st.image('https://media.giphy.com/media/CgzeCSpg4X0QEQxus6/giphy.gif')

    # Dados oriundos do GEO INFO - EMBRAPA - Rede de drenagem região semiárida de Alagoas
    hunger = gpd.read_file('http://geoinfo.cnps.embrapa.br/geoserver/wfs?srsName=EPSG%3A4326&typename=geonode%3Ahidrografia&outputFormat=json&version=1.0.0&service=WFS&request=GetFeature')
    m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Terrain', zoom_start=1.5)
    folium.Choropleth(
        geo_data=hunger,
        name='Percentual',
        fill_color='Reds',
    ).add_to(m)
    folium.LayerControl().add_to(m)
    # Mostrar folium map no streamlit
    folium_static(m)