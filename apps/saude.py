import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import pandas as pd
import pandas
import requests, zipfile, io
import xml.etree.ElementTree as Xet
import os
import requests
import xmltodict
import csv


def app(list_of_files=None):

    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-03.png')
    titl.title('ODS 3: Saúde e Bem-Estar')
    st.subheader('Garantir o acesso à saúde de qualidade e promover o bem-estar para todos, em todas as idades')

    with st.expander('Indicador 3.1'):
        st.write('Até 2030, reduzir a taxa de mortalidade materna global para menos de 70 mortes por 100.000 nascidos vivos')
    with st.expander('Indicador 3.2'):
        st.write('Até 2030, acabar com as mortes evitáveis de recém-nascidos e crianças menores de 5 anos, com todos os países objetivando reduzir a mortalidade neonatal para pelo menos 12 por 1.000 nascidos vivos e a mortalidade de crianças menores de 5 anos para pelo menos 25 por 1.000 nascidos vivos')
    with st.expander('Indicador 3.3'):
        st.write('Até 2030, acabar com as epidemias de AIDS, tuberculose, malária e doenças tropicais negligenciadas, e combater a hepatite, doenças transmitidas pela água, e outras doenças transmissíveis')
    with st.expander('Indicador 3.4'):
        st.write('Até 2030, reduzir em um terço a mortalidade prematura por doenças não transmissíveis via prevenção e tratamento, e promover a saúde mental e o bem-estar')
    with st.expander('Indicador 3.5'):
        st.write('Reforçar a prevenção e o tratamento do abuso de substâncias, incluindo o abuso de drogas entorpecentes e uso nocivo do álcool')
    with st.expander('Indicador 3.6'):
        st.write('Até 2020, reduzir pela metade as mortes e os ferimentos globais por acidentes em estradas')
    with st.expander('Indicador 3.7'):
        st.write('Até 2030, assegurar o acesso universal aos serviços de saúde sexual e reprodutiva, incluindo o planejamento familiar, informação e educação, bem como a integração da saúde reprodutiva em estratégias e programas nacionais')
    with st.expander('Indicador 3.8'):
        st.write('Atingir a cobertura universal de saúde, incluindo a proteção do risco financeiro, o acesso a serviços de saúde essenciais de qualidade e o acesso a medicamentos e vacinas essenciais seguros, eficazes, de qualidade e a preços acessíveis para todos')
    with st.expander('Indicador 3.9'):
        st.write('Até 2030, reduzir substancialmente o número de mortes e doenças por produtos químicos perigosos, contaminação e poluição do ar e água do solo')
    with st.expander('Indicador 3.a'):
        st.write('Fortalecer a implementação da Convenção-Quadro para o Controle do Tabaco em todos os países, conforme apropriado')
    with st.expander('Indicador 3.b'):
        st.write('Apoiar a pesquisa e o desenvolvimento de vacinas e medicamentos para as doenças transmissíveis e não transmissíveis, que afetam principalmente os países em desenvolvimento, proporcionar o acesso a medicamentos e vacinas essenciais a preços acessíveis, de acordo com a Declaração de Doha, que afirma o direito dos países em desenvolvimento de utilizarem plenamente as disposições do acordo TRIPS sobre flexibilidades para proteger a saúde pública e, em particular, proporcionar o acesso a medicamentos para todos')
    with st.expander('Indicador 3.c'):
        st.write('Aumentar substancialmente o financiamento da saúde e o recrutamento, desenvolvimento e formação, e retenção do pessoal de saúde nos países em desenvolvimento, especialmente nos países menos desenvolvidos e nos pequenos Estados insulares em desenvolvimento')
    with st.expander('Indicador 3.d'):
        st.write('Reforçar a capacidade de todos os países, particularmente os países em desenvolvimento, para o alerta precoce, redução de riscos e gerenciamento de riscos nacionais e globais de saúde')

    st.write('Para este objetivo, serão apresentados dados de **Casos de COVID-19 em Curitiba - PR**')
    st.write('A seguir, o relatório contendo as informações sobre o número de casos de COVID-19 no município de Curitiba.')

    url = 'https://ippuc.org.br/geodownloads/SHAPES_SIRGAS/DIVISA_DE_BAIRROS_SIRGAS.zip'
    filename = 'DIVISA_DE_BAIRROS.shp'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    df_bairros = gpd.read_file(filename, sep=',')

    url = "http://dadosabertos.c3sl.ufpr.br/curitiba/CasosCovid19/CasosCovid19.xml"
    response = requests.get(url)
    data = xmltodict.parse(response.content)

    #casos = 'C:/Users/rayss/PycharmProjects/Projeto2TCC/2022-03-03_Casos_Covid_19_-_Base_de_Dados.csv'
    casos = 'https://mid.curitiba.pr.gov.br/dadosabertos/CasosCovid19/2022-03-24_Casos_Covid_19_-_Base_de_Dados.csv'
    df_casos = pd.read_csv(casos, encoding='latin1', delimiter=';')
    casos_por_bairro = df_casos.groupby("BAIRRO")[['CLASSIFICAÇÃO FINAL']].count().reset_index()

    st.subheader('Mapa de casos por bairro')
    m = folium.Map(location=[-25.5, -49.3], tiles='Stamen Terrain', zoom_start=11)
    bins = list(casos_por_bairro['CLASSIFICAÇÃO FINAL'].quantile([0, 0.25, 0.5, 0.75, 1]))
    folium.Choropleth(
    geo_data=df_bairros,
    name='Casos por bairro',
    data=casos_por_bairro,
    columns=['BAIRRO', 'CLASSIFICAÇÃO FINAL'],
    key_on='feature.properties.NOME',
    fill_color='Reds',
    legend_name='Casos por bairro',
    bins=bins,
    labels={'BAIRRO'}
    ).add_to(m)

    folium.LayerControl().add_to(m)
    folium_static(m)

    table_days = st.slider('Escolha a quantidade de dias que você quer ver na tabela. ', min_value=3, max_value=15, value=5, step=1)

    st.subheader(f'Resumo dos últimos {table_days} casos de COVID-19.')
    st.markdown(""" Essa tabela apresenta a data, classificação, idade, sexo, bairro e status dos casos.""")

    a = df_casos.iloc[-table_days:, -8:]
    my_table = st.table(a)

    # Gráfico Total de Casos
    st.subheader(f'Total de casos por bairro.')
    total_cases_bairro = df_casos['BAIRRO'].value_counts()
    st.bar_chart(total_cases_bairro)

    st.subheader(f'Total de casos para Curitiba')
    total_cases_chart = df_casos['ENCERRAMENTO'].value_counts()
    st.bar_chart(total_cases_chart)
    st.markdown("""**OBS:** Você pode passar o mouse sobre a barra para ver a quantidade exata de casos e usar o mouse para aumentar ou diminuir o tamanho do gráfico.""")

    # with author_credits:
    st.subheader(f'Créditos')

    st.info("""\
        Os dados utilizado foram disponibilizados pela [Prefeitura Municipal de Curitiba](https://www.curitiba.pr.gov.br/dadosabertos/).
        
        Essa aplicação usa a biblioteca Streamlit. Disponível no [GitHub](https://github.com/rayssafig/Projeto2TCC)
    """)

