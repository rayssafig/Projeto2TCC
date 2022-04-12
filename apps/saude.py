import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import pandas as pd
import requests, zipfile, io


def app():

    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-03.png')
    titl.title('ODS 3: Saúde e Bem-Estar')
    st.subheader('Garantir o acesso à saúde de qualidade e promover o bem-estar para todos, em todas as idades')
    st.write('Cada ODS apresenta uma série de indicadores, que representam objetivos menores que auxiliam a atingir o objetivo principal. '
             'Você pode visualizar todos os indicadores e metas desenvolviddos para esse ODS, expandindo a seção a seguir')

    with st.expander('Saber mais sobre os Indicadores do Objetivo 3'):
        st.write('**3.1** Até 2030, reduzir a taxa de mortalidade materna global para menos de 70 mortes por 100.000 nascidos vivos')
        st.write('**3.2** Até 2030, acabar com as mortes evitáveis de recém-nascidos e crianças menores de 5 anos, com todos os países objetivando reduzir a mortalidade neonatal para pelo menos 12 por 1.000 nascidos vivos e a mortalidade de crianças menores de 5 anos para pelo menos 25 por 1.000 nascidos vivos')
        st.write('**3.3** Até 2030, acabar com as epidemias de AIDS, tuberculose, malária e doenças tropicais negligenciadas, e combater a hepatite, doenças transmitidas pela água, e outras doenças transmissíveis')
        st.write('**3.4** Até 2030, reduzir em um terço a mortalidade prematura por doenças não transmissíveis via prevenção e tratamento, e promover a saúde mental e o bem-estar')
        st.write('**3.5** Reforçar a prevenção e o tratamento do abuso de substâncias, incluindo o abuso de drogas entorpecentes e uso nocivo do álcool')
        st.write('**3.6** Até 2020, reduzir pela metade as mortes e os ferimentos globais por acidentes em estradas')
        st.write('**3.7** Até 2030, assegurar o acesso universal aos serviços de saúde sexual e reprodutiva, incluindo o planejamento familiar, informação e educação, bem como a integração da saúde reprodutiva em estratégias e programas nacionais')
        st.write('**3.8** Atingir a cobertura universal de saúde, incluindo a proteção do risco financeiro, o acesso a serviços de saúde essenciais de qualidade e o acesso a medicamentos e vacinas essenciais seguros, eficazes, de qualidade e a preços acessíveis para todos')
        st.write('**3.9** Até 2030, reduzir substancialmente o número de mortes e doenças por produtos químicos perigosos, contaminação e poluição do ar e água do solo')
        st.write('**3.a** Fortalecer a implementação da Convenção-Quadro para o Controle do Tabaco em todos os países, conforme apropriado')
        st.write('**3.c** Aumentar substancialmente o financiamento da saúde e o recrutamento, desenvolvimento e formação, e retenção do pessoal de saúde nos países em desenvolvimento, especialmente nos países menos desenvolvidos e nos pequenos Estados insulares em desenvolvimento')
        st.write('**3.d** Reforçar a capacidade de todos os países, particularmente os países em desenvolvimento, para o alerta precoce, redução de riscos e gerenciamento de riscos nacionais e globais de saúde')

    st.subheader('Mapeando casos de COVID-19')
    st.write('O cenário atual enfrentado pelo mundo nos últimos dois anos com a pandemia, enfatizou a necessidade de consumir dados atualizados e precisos. '
             'Adicionalmente, os dados geoespaciais, contribuem significativamente na representação das informações. ' )
    st.write('Combinando dados estatísticos e mapas, pode-se não só passar uma mensagem clara e de fácil entendimento ao usuário, como também é uma das formas '
             'de contribuir com o ODS 3, ao levantar informações relevantes como a dos casos da doença em um município, e a sustentar o **Indicador 3.b**. '
             'Portanto, serão apresentados dados de **Casos de COVID-19 em Curitiba - PR**')
    with st.expander('Mais detallhes sobre o Indicador 3.b'):
        st.write('**Indicador 3.b:** "Apoiar a pesquisa e o desenvolvimento de vacinas e medicamentos para as doenças transmissíveis e não transmissíveis, que afetam principalmente os países em desenvolvimento, proporcionar o acesso a medicamentos e vacinas essenciais a preços acessíveis, '
             'de acordo com a Declaração de Doha, que afirma o direito dos países em desenvolvimento de utilizarem plenamente as disposições do acordo TRIPS sobre flexibilidades para proteger a saúde pública e, em particular, proporcionar o acesso a medicamentos para todos."')
    st.write(
        'A seguir, o relatório contendo as informações sobre o número de casos de COVID-19 no município de Curitiba.')

    url = 'https://ippuc.org.br/geodownloads/SHAPES_SIRGAS/DIVISA_DE_BAIRROS_SIRGAS.zip'
    filename = 'DIVISA_DE_BAIRROS.shp'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    df_bairros = gpd.read_file(filename, sep=',')

    casos = 'https://mid.curitiba.pr.gov.br/dadosabertos/CasosCovid19/2022-04-06_Casos_Covid_19_-_Base_de_Dados.csv'
    df_casos = pd.read_csv(casos, encoding='latin1', delimiter=';')
    casos_por_bairro = df_casos.groupby("BAIRRO")[['CLASSIFICAÇÃO FINAL']].count().reset_index()
    join = pd.merge(df_bairros, df_casos, left_on="NOME", right_on="BAIRRO")

    st.subheader('Mapa de casos da doença por bairro de Curitiba - PR')
    m = folium.Map(location=[-25.5, -49.3], tiles='Stamen Terrain', zoom_start=11, control_scale=True)
    bins = list(casos_por_bairro['CLASSIFICAÇÃO FINAL'].quantile([0, 0.1, 0.75, 0.9, 0.98, 1]))
    folium.Choropleth(
        geo_data=df_bairros,
        name='Casos por bairro',
        data=casos_por_bairro,
        columns=['BAIRRO', 'CLASSIFICAÇÃO FINAL'],
        key_on='feature.properties.NOME',
        fill_color='BuPu',
        legend_name='Casos por bairro',
        bins=bins,
        labels={'BAIRRO'},
        tooltip=folium.features.GeoJsonTooltip(fields=['BAIRRO'], localize=True)
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
        df_bairros,
        style_function=style_function,
        control=False,
        highlight_function=highlight_function,
        tooltip=folium.features.GeoJsonTooltip(
            fields=['NOME'],
            aliases=['Nome do bairro: '],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"))
    )
    m.add_child(NIL)
    m.keep_in_front(NIL)
    folium.LayerControl().add_to(m)
    folium_static(m)

    st.subheader('Informações sobre os casos da doença')
    st.markdown(""" Essa tabela apresenta a data, classificação, idade, sexo, bairro e status dos casos.""")
    table_days = st.slider('Escolha a quantidade de casos que você quer ver na tabela. ', min_value=3, max_value=15,
                           value=5, step=1)
    st.write(f'**Resumo dos últimos {table_days} casos de COVID-19.**')
    a = df_casos.iloc[-table_days:, -8:]
    my_table = st.table(a)

    # Gráfico Total de Casos
    st.subheader(f'Total de casos por bairro.')
    total_cases_bairro = df_casos['BAIRRO'].value_counts()
    st.bar_chart(total_cases_bairro)

    st.subheader(f'Total de casos para Curitiba')
    total_cases_chart = df_casos['ENCERRAMENTO'].value_counts()
    st.bar_chart(total_cases_chart)
    st.markdown(
        """**OBS:** Você pode passar o mouse sobre a barra para ver a quantidade exata de casos e usar o mouse para aumentar ou diminuir o tamanho do gráfico.""")

    st.subheader('Fonte dos dados')
    st.info("""
        \n 🔍 Os dados de **COVID-19** estão disponíveis no [Portal de dados abertos](https://www.curitiba.pr.gov.br/dadosabertos/) da Prefeitura Municipal de Curitiba.
        \n 🔍 Os **dados espaciais** do município são disponibilizados pelo [IPPUC](https://ippuc.org.br/geodownloads) - Instituto de Pesquisa e Planejamento Urbano de Curitiba.""")

