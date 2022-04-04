import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import geopandas
from matplotlib import pyplot
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px


def app():
    global data
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-02.png')
    titl.title('ODS 2: Fome zero e agricultura sustentável')
    st.subheader('Erradicar a fome, alcançar a segurança alimentar, '
                 'melhorar a nutrição e promover a agricultura sustentável')

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
    casos_por_bairro = hunger.groupby("max_year")[['latest_value']].count().reset_index()
    st.write(casos_por_bairro)
    hunger.plot()
    #st.write(pyplot.show())
    # Gráfico Total de Casos
    st.subheader(f'Total de casos por bairro.')
    x=hunger['years'].value_counts()
    fig = px.line(hunger, x, y=hunger['latest_value'])
    fig.show()

    st.subheader(f'Total de casos para Curitiba')
    total_cases_chart = hunger['ENCERRAMENTO'].value_counts()
    st.bar_chart(total_cases_chart)

    m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Terrain', zoom_start=1.5)
    folium.GeoJson(
        hunger,
        name='Percentual',
        popup="última proporção conhecida: ",
        tooltip=folium.features.GeoJsonTooltip(fields=['latest_value'], localize=True)
    ).add_to(m)
    folium.LayerControl().add_to(m)
    # Mostrar folium map no streamlit
    folium_static(m)

    st.altair_chart(hunger)

    df = pd.DataFrame(
        {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
         'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
         'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
         'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
    gdf = geopandas.GeoDataFrame(
        df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
    st.write(gdf.head())
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')
    gdf.plot(ax=ax, color='red')
    st.pyplot()
