import streamlit as st
import geopandas as gpd
import pandas as pd
from streamlit_folium import folium_static
import folium
import requests, zipfile, io
from pathlib import Path
import leafmap.foliumap as leafmap
import ast


def app():
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-06.png')
    titl.title('ODS 6: Água potável e saneamento')
    st.subheader('Garantir a disponibilidade e a gestão sustentável da água potável e do saneamento para todos')

    with st.expander('Indicadores do Objetivo 6'):
        st.write("""**6.1** Até 2030, alcançar o acesso universal e equitativo a água potável e segura para todos
        \n **6.2** Até 2030, alcançar o acesso a saneamento e higiene adequados e equitativos para todos, e acabar com a defecação a céu aberto, com especial atenção para as necessidades das mulheres e meninas e daqueles em situação de vulnerabilidade
        \n **6.3** Até 2030, melhorar a qualidade da água, reduzindo a poluição, eliminando despejo e minimizando a liberação de produtos químicos e materiais perigosos, reduzindo à metade a proporção de águas residuais não tratadas e aumentando substancialmente a reciclagem e reutilização segura globalmente
        \n **6.4** Até 2030, aumentar substancialmente a eficiência do uso da água em todos os setores e assegurar retiradas sustentáveis e o abastecimento de água doce para enfrentar a escassez de água, e reduzir substancialmente o número de pessoas que sofrem com a escassez de água
        \n **6.5** Até 2030, implementar a gestão integrada dos recursos hídricos em todos os níveis, inclusive via cooperação transfronteiriça, conforme apropriado
        \n **6.6** Até 2020, proteger e restaurar ecossistemas relacionados com a água, incluindo montanhas, florestas, zonas úmidas, rios, aquíferos e lagos
        \n **6.a** Até 2030, ampliar a cooperação internacional e o apoio à capacitação para os países em desenvolvimento em atividades e programas relacionados à água e saneamento, incluindo a coleta de água, a dessalinização, a eficiência no uso da água, o tratamento de efluentes, a reciclagem e as tecnologias de reuso
        \n **6.b** Apoiar e fortalecer a participação das comunidades locais, para melhorar a gestão da água e do saneamento""")
    
    st.subheader('Represa do Iraí')
    st.write('Afim de atingir o Indicador 6.6, pode-se observar o reservatório de água, ao longo do tempo, e como foi afetado pela forte estiagem nos últimos três anos. Mapear a represa do Iraí, que abastece Curitiba e região metropolitana, é uma das formas de proteger esse ecossistema. ')
    st.image('https://media.giphy.com/media/CgzeCSpg4X0QEQxus6/giphy.gif')

    st.subheader('Indicador xxx')
    # http://geoinfo.cnps.embrapa.br/layers/geonode%3Ahidrografia#more
    # https://dados.gov.br/dataset?tags=Geoespacial&organization=instituto-brasileiro-de-geografia-e-estatistica-ibge

    # Dados oriundos do GEO INFO - EMBRAPA - Rede de drenagem região semiárida de Alagoas
    st.subheader('Rede de drenagem região semiárida de Alagoas')
    drenagem = gpd.read_file('http://geoinfo.cnps.embrapa.br/geoserver/wfs?srsName=EPSG%3A4326&typename=geonode%3Ahidrografia&outputFormat=json&version=1.0.0&service=WFS&request=GetFeature')
    m = folium.Map(location=[-9.4, -37.3], tiles='Stamen Terrain', zoom_start=9, control_scale=True)
    folium.Choropleth(
        geo_data=drenagem,
        name='Percentual',
        fill_color='Reds',
    ).add_to(m)
    folium.LayerControl().add_to(m)
    # Mostrar folium map no streamlit
    folium_static(m)

    API_key = 'a68baa372ad3b37c3ec0e77c4d7ce0b3'
    #request = requests.get('http://api.openweathermap.org/geo/1.0/reverse?lat={}&lon={lon}&limit={limit}&appid={API_key}'.format(lat) )

    'https://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid={API key}'

    LOCATION = '*******'
    # lat=-25.480877 e lon=-49.304424
    #LATITUDE = st.text_input("Search for a lat:", "")
    LATITUDE = '-25.480877'
    LONGITUDE = '-49.304424'
    UNITS = 'imperial'
    CSV_OPTION = True  # if csv_option == True, a weather data will be appended to 'record.csv'
    BASE_URL = 'http://api.openweathermap.org/data/2.5/onecall?'
    URL = BASE_URL + 'lat=' + LATITUDE + '&lon=' + LONGITUDE + '&units=' + UNITS + '&appid=' + API_key

    response = requests.get(URL)
    st.write(response)
    data = response.json()
    st.write(data)
    gdf = pd.read_json(response)

    style = {'fillColor': '#f5f5f5', 'lineColor': '#ffffbf'}
    m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Terrain', zoom_start=1.5, control_scale=True)
    folium.GeoJson(
        gdf,
        name='Proporção em %',
        style_function=lambda x: style,
        popup="última proporção conhecida: ",
    ).add_to(m)
    folium.LayerControl().add_to(m)
    folium_static(m)

    @st.cache
    def get_layers(url1):
        options = leafmap.get_wms_layers(url1)
        return options

    layers = None
    url1 = 'https://geo.socioambiental.org/webadaptor2/services/raisg/raisg_tis_d/MapServer/WMSServer?request=GetCapabilities&service=WMS'
    m = leafmap.Map(center=(36.3, 0), zoom=2, control_scale=True)
    if layers is not None:
        for layer in layers:
            m.add_wms_layer(
                url1, layers=layer, name=layer, attribution=" ", transparent=True
            )
    m.to_streamlit(800,600)
    folium_static(m)

    st.subheader('Fonte dos dados:')
    st.info("""
            \n 🔍 """)
