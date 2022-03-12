import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import pandas as pd
#import Fiona


def app():

    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-03.png')
    titl.title('ODS 3: Saúde e Bem-Estar')
    st.subheader('Garantir o acesso à saúde de qualidade e promover o bem-estar para todos, em todas as idades')

    st.write('Para este objetivo, serão apresentados dados de **Casos de COVID-19 em Curitiba - PR**')
    #st.subheader("Secretaria de Saúde de Curitiba")
    st.write('A seguir, o relatório contendo as informações sobre o número de casos de COVID-19 no município de Curitiba.')

    bairros = 'C:/Users/rayss/PycharmProjects/Projeto2TCC/bairros_novo.geojson'
    df_bairros = gpd.read_file(bairros)
    casos = 'C:/Users/rayss/PycharmProjects/Projeto2TCC/2022-03-03_Casos_Covid_19_-_Base_de_Dados.csv'
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
    key_on='feature.properties.BAIRRO',
    fill_color='Reds',
    legend_name='Casos por bairro',
    bins=bins
    ).add_to(m)

    folium.LayerControl().add_to(m)
    folium_static(m)

    #def main():
     #   with user_input:
    table_days = st.slider('Escolha a quantidade de dias que você quer ver na tabela. ', min_value=3, max_value=15, value=5, step=1)

    #with output_graphs:
    st.subheader(f'Resumo dos últimos {table_days} casos de COVID-19.')
    st.markdown(""" Essa tabela apresenta a data, classificação, idade, sexo, bairro e status dos casos.""")

    a = df_casos.iloc[-table_days:, -8:]
    my_table = st.table(a)

    # Total Cases Graph
    st.subheader(f'Total de casos por bairro.')
    total_cases_bairro = df_casos['BAIRRO'].value_counts()
    st.bar_chart(total_cases_bairro)

    st.subheader(f'Total de casos para Curitiba')
    total_cases_chart = df_casos['ENCERRAMENTO'].value_counts()
    st.bar_chart(total_cases_chart)
    st.markdown("""**OBS:** Você pode passar o mouse sobre a barra para ver a quantidade exata de casos e usar o mouse para aumentar ou diminuir o tamanho do gráfico.""")

    # with author_credits:
    st.subheader(f'Créditos')
    st.markdown("""
    **Obrigada por utilizar minha aplicação!** """)

    st.info("""\
        Os dados utilizado foram disponibilizados pela [Prefeitura Municipal de Curitiba](https://www.curitiba.pr.gov.br/dadosabertos/).
        
        Essa aplicação usa a biblioteca Streamlit. Disponível no [GitHub](https://github.com/rayssafig/Projeto2TCC)
    """)

    #if __name__ == '__main__':
    #main()

