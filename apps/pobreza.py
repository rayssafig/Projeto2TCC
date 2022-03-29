import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import pandas as pd
import plotly.express as px
import requests, zipfile, io
from plotnine import *
import matplotlib.pyplot as plt
import geobr
from geobr import read_municipality
from streamlit_observable import observable
import leafmap.foliumap as leafmap

from geopy.geocoders import Nominatim


def app():

    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-01.png')
    titl.title('ODS 1: Erradicação da pobreza')
    st.subheader('Objetivo 1: Erradicar a pobreza em todas as formas e em todos os lugares')
    st.write('Cada ODS apresenta uma série de indicadores, que representam objetivos menores que auxiliam a atingir o objetivo principal. '
             'Você pode visualizar todos os indicadores criados para esse ODS, expandindo a seção a seguir.')

    with st.expander(label='Mapeando o Indicador 1.1'):
        st.write('**1.1** Até 2030, erradicar a pobreza extrema para todas as pessoas em todos os lugares, atualmente medida como pessoas vivendo com menos de US$ 1,90 por dia')
        st.write(
            '**Proporção da população abaixo da linha de pobreza internacional (em porcentagem):**')
        st.write(
            'A proporção da população que vive abaixo da linha de pobreza extrema caiu de 22% em 1990 para 4% em 2018.')

        poverty = gpd.read_file(
            'https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SI_POV_DAY1_1_1_1_2020Q2G03/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson')
        poverty1 = gpd.read_file(
            'https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SI_POV_DAY1_1_1_1_2020Q2G03/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

        m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Terrain', zoom_start=1.5)
        folium.Choropleth(
            geo_data=poverty1,
            name='Percentual',
            fill_color='Reds',
            popup='Latest Value'
        ).add_to(m)
        folium.LayerControl().add_to(m)
        # Mostrar folium map no streamlit
        folium_static(m)

    with st.expander(label='Mapeando o Indicador 1.2'):
        st.write(
            '**1.2** Até 2030, reduzir pelo menos à metade a proporção de homens, mulheres e crianças, de todas as idades, que vivem na pobreza, em todas as suas dimensões, de acordo com as definições nacionais')
        st.write(
        '**Resultado do PIB per capita dos países, ao longo dos anos:** Mapear situação de renda da população global')

        # Bases de dados da biblioteca Ploty (Gapminder)
        df = pd.DataFrame(px.data.gapminder())
        df.head(5)
        a = df.iloc[:, :]
        clist = df['country'].unique()
        country = st.selectbox("Selecione um país:", clist)
        fig = px.line(df[df['country'] == country],
                      x="year", y="gdpPercap", title=f'Você está visualizando o PIB do país selecionado: {country}')
        st.plotly_chart(fig)
        st.write(df.head())
        st.write(clist)

        #mapa = gpd.read_file('https://services.arcgis.com/BG6nSlhZSAWtExvp/arcgis/rest/services/Baker_Global_Country_Codes/FeatureServer?f=pjson')

        url = 'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural' \
              '/ne_110m_admin_0_countries.zip '
        filename = 'ne_110m_admin_0_countries.shp'
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
        mapa = gpd.read_file(filename, sep=';')
        #mapa = gpd.read_file('https://github.com/datasets/geo-countries/blob/master/data/countries.geojson')
        #ISO3166-1-Alpha-3

        m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Terrain', zoom_start=1.5)
        folium.Choropleth(
            geo_data=mapa,
            name='Casos por bairro',
            data=df,
            #columns=['BAIRRO', 'CLASSIFICAÇÃO FINAL'],
            key_on='feature.properties.Alpha-3_code_ISO3166-1',
            fill_color='Reds',
            legend_name='Casos por bairro',
            #labels={'BAIRRO'}
        ).add_to(m)
        folium_static(m)


    with st.expander(label='Demais Indicadores do Objetivo 1'):
        st.write('**1.3** Implementar, em nível nacional, medidas e sistemas de proteção social adequados, para todos, incluindo pisos, e até 2030 atingir a cobertura substancial dos pobres e vulneráveis')
        st.write('**1.4** Até 2030, garantir que todos os homens e mulheres, particularmente os pobres e vulneráveis, tenham direitos iguais aos recursos econômicos, bem como o acesso a serviços básicos, propriedade e controle sobre a terra e outras formas de propriedade, herança, recursos naturais, novas tecnologias apropriadas e serviços financeiros, incluindo microfinanças')
        st.write('**1.5** Até 2030, construir a resiliência dos pobres e daqueles em situação de vulnerabilidade, e reduzir a exposição e vulnerabilidade destes a eventos extremos relacionados com o clima e outros choques e desastres econômicos, sociais e ambientais')
        st.write('**1.a** Garantir uma mobilização significativa de recursos a partir de uma variedade de fontes, inclusive por meio do reforço da cooperação para o desenvolvimento, para proporcionar meios adequados e previsíveis para que os países em desenvolvimento, em particular os países menos desenvolvidos, implementem programas e políticas para acabar com a pobreza em todas as suas dimensões')
        st.write('**1.b** Criar marcos políticos sólidos em níveis nacional, regional e internacional, com base em estratégias de desenvolvimento a favor dos pobres e sensíveis a gênero, para apoiar investimentos acelerados nas ações de erradicação da pobreza')

    st.info("""Fonte de dados:
            \n **UN DESA Statistics Division**, disponível em: https://unstats.un.org/sdgs/metadata/
            \n **Gapminder**, biblioteca Ploty, disponível em: https://www.gapminder.org/""")
    # Gráfico Total de Casos
    #geobr.list_geobr()
    #df = geobr.read_state(code_state="DF", year=2020)
    #df.plot()
