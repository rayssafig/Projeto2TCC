import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import requests, zipfile, io
import leafmap.foliumap as leafmap
import geopandas
from matplotlib import pyplot
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px
import functools

chart = functools.partial(st.plotly_chart, use_container_width=True)
COMMON_ARGS = {
    "color": "parentName",
    "color_discrete_sequence": px.colors.sequential.Cividis,
    "hover_data": [
        'latest_value',
    ],
}


def app():
    global data
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-02.png')
    titl.title('ODS 2: Fome zero e agricultura sustentável')
    st.subheader('Erradicar a fome, alcançar a segurança alimentar, '
                 'melhorar a nutrição e promover a agricultura sustentável')

    with st.expander('Saber mais sobre os Indicadores do Objetivo 2'):
        st.write("""**2.1** Até 2030, acabar com a fome e garantir o acesso de todas as pessoas, em particular os pobres e pessoas em situações vulneráveis, incluindo crianças, a alimentos seguros, nutritivos e suficientes durante todo o ano 
        \n **2.2** Até 2030, acabar com todas as formas de desnutrição, incluindo atingir, até 2025, as metas acordadas internacionalmente sobre nanismo e caquexia em crianças menores de cinco anos de idade, e atender às necessidades nutricionais dos adolescentes, mulheres grávidas e lactantes e pessoas idosas
        \n **2.3** Até 2030, dobrar a produtividade agrícola e a renda dos pequenos produtores de alimentos, particularmente das mulheres, povos indígenas, agricultores familiares, pastores e pescadores, inclusive por meio de acesso seguro e igual à terra, outros recursos produtivos e insumos, conhecimento, serviços financeiros, mercados e oportunidades de agregação de valor e de emprego não agrícola
        \n **2.4** Até 2030, garantir sistemas sustentáveis de produção de alimentos e implementar práticas agrícolas resilientes, que aumentem a produtividade e a produção, que ajudem a manter os ecossistemas, que fortaleçam a capacidade de adaptação às mudanças climáticas, às condições meteorológicas extremas, secas, inundações e outros desastres, e que melhorem progressivamente a qualidade da terra e do solo
        \n **2.5** Até 2020, manter a diversidade genética de sementes, plantas cultivadas, animais de criação e domesticados e suas respectivas espécies selvagens, inclusive por meio de bancos de sementes e plantas diversificados e bem geridos em nível nacional, regional e internacional, e garantir o acesso e a repartição justa e equitativa dos benefícios decorrentes da utilização dos recursos genéticos e conhecimentos tradicionais associados, como acordado internacionalmente
        \n **2.a** Aumentar o investimento, inclusive via o reforço da cooperação internacional, em infraestrutura rural, pesquisa e extensão de serviços agrícolas, desenvolvimento de tecnologia, e os bancos de genes de plantas e animais, para aumentar a capacidade de produção agrícola nos países em desenvolvimento, em particular nos países menos desenvolvidos
        \n **2.b** Corrigir e prevenir as restrições ao comércio e distorções nos mercados agrícolas mundiais, incluindo a eliminação paralela de todas as formas de subsídios à exportação e todas as medidas de exportação com efeito equivalente, de acordo com o mandato da Rodada de Desenvolvimento de Doha
        \n **2.c** Adotar medidas para garantir o funcionamento adequado dos mercados de commodities de alimentos e seus derivados, e facilitar o acesso oportuno à informação de mercado, inclusive sobre as reservas de alimentos, a fim de ajudar a limitar a volatilidade extrema dos preços dos alimentos""")
    
    hunger = gpd.read_file(
        'https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SN_ITK_DEFC_2_1_1_2020Q2G03/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson')

    st.subheader('Prevalência de subnutrição por país')
    m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Terrain', zoom_start=1.5, control_scale=True)
    folium.GeoJson(
        hunger,
        name='Percentual',
        popup="última proporção conhecida: ",
        tooltip=folium.features.GeoJsonTooltip(
            fields=['geoAreaName', 'latest_value'],
            aliases=['País (Área geográfica): ', 'Prevalência de desnutrição (%): '],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),
            localize=True)
    ).add_to(m)
    folium.LayerControl().add_to(m)
    folium_static(m)

    #pol_par = hunger['latest_value'].value_counts()
    pol_par = hunger.groupby("geoAreaName")[['latest_value']].sum().reset_index()
    # merge the two dataframe to get a column with the color
    df = pd.concat([pd.DataFrame(pol_par), hunger])
    colors = df['ISO3'].tolist()
    #st.write(pol_par)
    st.write(hunger)
    st.write(pol_par)

    filepath = gpd.read_file(
        "https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/AG_PRD_FIESSIN_2_1_2_2020Q2G03/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")

    # Gráfico Total de Casos
    st.subheader(f'Total de casos por bairro.')
    total_cases_bairro = filepath['sex_desc'].value_counts()
    st.bar_chart(total_cases_bairro)

    st.subheader(f'Taxa de analfabetismo por  Região')
    crop = filepath['sex_desc']
    fig = px.pie(filepath, values="latest_value", names="sex_desc", **COMMON_ARGS)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    chart(fig)

    st.subheader("Value of each Symbol per Account")
    fig = px.sunburst(
        filepath, path=["age_desc", "sex_desc"], values="latest_value", **COMMON_ARGS
    )
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    chart(fig)

    st.subheader('Fonte dos dados:')
    st.info("""
                \n 🔍 """)
