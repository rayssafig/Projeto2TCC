import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import pandas as pd
import plotly.express as px
import requests, zipfile, io


def app():

    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-01.png')
    titl.title('ODS 1: Erradicação da pobreza')
    st.subheader('Objetivo 1: Erradicar a pobreza em todas as formas e em todos os lugares')
    st.write('Cada ODS apresenta uma série de indicadores, que representam objetivos menores que auxiliam a atingir o objetivo principal. '
             'Você pode visualizar todos os indicadores criados para esse ODS, expandindo a seção a seguir.')

    with st.expander(label='Indicadores do Objetivo 1'):
        st.write('**1.1** Até 2030, erradicar a pobreza extrema para todas as pessoas em todos os lugares, atualmente medida como pessoas vivendo com menos de US$ 1,90 por dia')
        st.write('**1.2** Até 2030, reduzir pelo menos à metade a proporção de homens, mulheres e crianças, de todas as idades, que vivem na pobreza, em todas as suas dimensões, de acordo com as definições nacionais')
        st.write('**1.3** Implementar, em nível nacional, medidas e sistemas de proteção social adequados, para todos, incluindo pisos, e até 2030 atingir a cobertura substancial dos pobres e vulneráveis')
        st.write('**1.4** Até 2030, garantir que todos os homens e mulheres, particularmente os pobres e vulneráveis, tenham direitos iguais aos recursos econômicos, bem como o acesso a serviços básicos, propriedade e controle sobre a terra e outras formas de propriedade, herança, recursos naturais, novas tecnologias apropriadas e serviços financeiros, incluindo microfinanças')
        st.write('**1.5** Até 2030, construir a resiliência dos pobres e daqueles em situação de vulnerabilidade, e reduzir a exposição e vulnerabilidade destes a eventos extremos relacionados com o clima e outros choques e desastres econômicos, sociais e ambientais')
        st.write('**1.a** Garantir uma mobilização significativa de recursos a partir de uma variedade de fontes, inclusive por meio do reforço da cooperação para o desenvolvimento, para proporcionar meios adequados e previsíveis para que os países em desenvolvimento, em particular os países menos desenvolvidos, implementem programas e políticas para acabar com a pobreza em todas as suas dimensões')
        st.write('**1.b** Criar marcos políticos sólidos em níveis nacional, regional e internacional, com base em estratégias de desenvolvimento a favor dos pobres e sensíveis a gênero, para apoiar investimentos acelerados nas ações de erradicação da pobreza')

    st.write('A pobreza e a pobreza extrema são pautas amplamente discutidas ao redor do mundo para tentar mitigar o problema. Erradicar a pobreza em todas as suas formas é o primeiro Objetivo de Desenvolvimento Sustentável e já se caracteriza como um objetivo desafiador,'
             ' pois ao mesmo tempo que tem se visto que o número de pessoas que vive em situação de extrema pobreza diminuiu em mais da metade entre 1990 e 2015, passando de 1.9 bilhão para 836 milhões, muitos ainda sofrem para ter acesso às necessidades básicas do ser humano. ')
    st.write(
        '**Indicador 1.1: Mapeando a população que vive abaixo da linha de pobreza internacional**')
    st.write('Buscar atingir o ODS é assumir um comprometimento ousado mas importante para dar visibilidade aos mais vulneráveis, apoiar comunidades que sustentam a causa e a satisfazer o acesso a serviços básicos da sociedade.')

    st.write(
        """A proporção da população que vive abaixo da linha de pobreza extrema caiu de 22% em 1990 para 4% em 2018.
        O mapa a seguir mostra a taxa (em porcentagem) da população que vive abaixo dessa linha, por país.""")

    poverty1 = gpd.read_file(
        'https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SI_POV_DAY1_1_1_1_2020Q2G03/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson')

    style = {'fillColor': '#f5f5f5', 'lineColor': '#ffffbf'}
    st.subheader('Taxa da população que vive abaixo da linha da pobreza por país')
    m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Terrain', zoom_start=1.5, control_scale=True)
    folium.GeoJson(
        poverty1,
        name='Proporção em %',
        style_function=lambda x: style,
        popup="última proporção conhecida: ",
        tooltip=folium.features.GeoJsonTooltip(
            fields=['geoAreaName', 'latest_value'],
            aliases=['País (Área geográfica): ', 'Proporção da população (%): '],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px; icon=icon"),
            localize=True)
    ).add_to(m)
    folium.LayerControl().add_to(m)
    folium_static(m)
    st.write('**OBS:** Os valores são referentes ao último ano de dados disponíveis.')

    st.write('**Mapeando o PIB per capita interno dos países**')
    with st.expander('Indicador 1.2'):
        st.write('**1.2** Até 2030, reduzir pelo menos à metade a proporção de homens, mulheres e crianças, de todas as idades, que vivem na pobreza, em todas as suas dimensões, de acordo com as definições nacionais')
    st.write('Para atingir o Indicador 1.2, é importante conhecer as diferentes realidades de cada país, e suas definições internas. Dessa forma, é possível mapear o resultado do PIB nacional e visualizar a sua evolução '
             'ao longo do tempo, para entender e quantificar os resultados.')
    st.write('**Resultado do PIB per capita dos países, ao longo dos anos:** Mapear situação de renda da população global')

    # Bases de dados da biblioteca Ploty (Gapminder)
    df = pd.DataFrame(px.data.gapminder())
    df.head(5)
    a = df.iloc[:, :]
    clist = df['country'].unique()
    country = st.selectbox("Selecione um país:", clist)
    fig = px.line(df[df['country'] == country],
                  x="year", y="gdpPercap", title=f'Você está visualizando o PIB do país selecionado: {country}')
    st.plotly_chart(fig)
    st.write(df)
    #st.write(clist)

    url = 'http://www.labgeolivre.ufpr.br/arquivos/ne_110m_admin_0_countries.zip'
    filename = 'ne_110m_admin_0_countries.shp'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    mapa = gpd.read_file(filename, sep=',')
    #st.write(casos)
    group = df.groupby('country')[['iso_alpha']].count()
    st.write(group)
    Join = pd.merge(mapa, df, left_on="ISO_A3_EH", right_on="iso_alpha")
    casos = Join.groupby("gdpPercap")[['country']].count().reset_index()
    #st.write(Join.head(-2))
    st.write(mapa.head(2))

    st.subheader('**Veja o PIB per capita por país no mapa:**')
    m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Terrain', zoom_start=1.5, control_scale=True)
    bins = list(mapa['POP_EST'].quantile([0, 0.1, 0.75, 0.9, 0.98, 1]))
    folium.Choropleth(
        geo_data=Join,
        name='Países',
        #data=df,
        #columns=['country', 'gdpPercap'], #coluna
        key_on='feature.properties.POP_EST',
        fill_color='Reds',
        legend_name='PIB per capita',
        bins=bins,
        #labels={'NAME'}
    ).add_to(m)
    style_function = lambda x: {'fillColor': '#ffffff',
                                'color': '#000000',
                                'fillOpacity': 0,
                                'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000',
                                    'color': '#000000',
                                    'fillOpacity': 0,
                                    'weight': 0.1}
    NIL = folium.features.GeoJson(
        Join,
        style_function=style_function,
        control=False,
        highlight_function=highlight_function,
        tooltip=folium.features.GeoJsonTooltip(
            fields=['NAME', 'gdpPercap'],
            aliases=['Nome do país: ', 'PIB per capita:'],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"))
    )
    m.add_child(NIL)
    m.keep_in_front(NIL)
    folium.LayerControl().add_to(m)
    folium_static(m)


    st.subheader('Fonte dos dados:')
    st.info("""
            \n 🔍 Conjunto de dados espaciais de domínio público [Natural Earth](https://www.naturalearthdata.com/downloads/)
            \n 🔍 Divisão de Estatística das Nações Unidas [UN DESA Statistics Division](https://unstats.un.org/sdgs/dataportal)
            \n 🔍 Dados da biblioteca Ploty [Gapminder](https://www.gapminder.org/)""")
    # Gráfico Total de Casos
    #geobr.list_geobr()
    #df = geobr.read_state(code_state="DF", year=2020)
    #df.plot()
