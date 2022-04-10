import streamlit as st
import requests, zipfile, io
import geopandas as gpd
import pandas as pd
from streamlit_folium import folium_static
import folium


def app():
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-04.png')
    titl.title('ODS 4: Educação de qualidade')
    st.subheader('Garantir o acesso à educação inclusiva, de qualidade e equitativa, e promover oportunidades de aprendizagem ao longo da vida para todos')
    st.write('A fim de alcançar uma educação de qualidade para uma nação, é importante e necessário conhecer a realidade daquele local, levantar dados, desde os mais '
             'básicos, para poder entender a situação e aplicar políticas eficientes que tragam resultados. '
             'Você pode visualizar todos os indicadores e metas desenvolviddos para esse ODS, expandindo a seção a seguir')

    with st.expander('Saber mais sobre os Indicadores do Objetivo 4'):
        st.write('**4.1** Até 2030, garantir que todas as meninas e meninos completem o ensino primário e secundário livre, equitativo e de qualidade, que conduza a resultados de aprendizagem relevantes e eficazes')
        st.write('**4.2** Até 2030, garantir que todos as meninas e meninos tenham acesso a um desenvolvimento de qualidade na primeira infância, cuidados e educação pré-escolar, de modo que eles estejam prontos para o ensino primário')
        st.write('**4.3** Até 2030, assegurar a igualdade de acesso para todos os homens e mulheres à educação técnica, profissional e superior de qualidade, a preços acessíveis, incluindo universidade ')
        st.write('**4.4** Até 2030, aumentar substancialmente o número de jovens e adultos que tenham habilidades relevantes, inclusive competências técnicas e profissionais, para emprego, trabalho decente e empreendedorismo')
        st.write('**4.5** Até 2030, eliminar as disparidades de gênero na educação e garantir a igualdade de acesso a todos os níveis de educação e formação profissional para os mais vulneráveis, incluindo as pessoas com deficiência, povos indígenas e as crianças em situação de vulnerabilidade')
        st.write('**4.6** Até 2030, garantir que todos os jovens e uma substancial proporção dos adultos, homens e mulheres estejam alfabetizados e tenham adquirido o conhecimento básico de matemática')
        st.write('**4.7** Até 2030, garantir que todos os alunos adquiram conhecimentos e habilidades necessárias para promover o desenvolvimento sustentável, inclusive, entre outros, por meio da educação para o desenvolvimento sustentável e estilos de vida sustentáveis, '
                 'direitos humanos, igualdade de gênero, promoção de uma cultura de paz e não violência, cidadania global e valorização da diversidade cultural e da contribuição da cultura para o desenvolvimento sustentável')
        st.write('**4.a** Construir e melhorar instalações físicas para educação, apropriadas para crianças e sensíveis às deficiências e ao gênero, e que proporcionem ambientes de aprendizagem seguros e não violentos, inclusivos e eficazes para todos')
        st.write('**4.b** Até 2020, substancialmente ampliar globalmente o número de bolsas de estudo para os países em desenvolvimento, em particular os países menos desenvolvidos, pequenos Estados insulares em desenvolvimento e os países africanos, para o ensino superior, incluindo programas '
                 'de formação profissional, de tecnologia da informação e da comunicação, técnicos, de engenharia e programas científicos em países desenvolvidos e outros países em desenvolvimento')
        st.write('**4.c** Até 2030, substancialmente aumentar o contingente de professores qualificados, inclusive por meio da cooperação internacional para a formação de professores, nos países em desenvolvimento, especialmente os países menos desenvolvidos e pequenos Estados insulares em desenvolvimento')

    # Fonte: IBGE
    url = 'https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2021/Brasil/BR/BR_UF_2021.zip'
    filename = 'BR_UF_2021.shp'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    df_BR = gpd.read_file(filename, sep=',')
    #st.write(df_BR.head())

    # Fonte: IPEA DATA - Instituto de Pesquisa Econômica Aplicada
    tabela = 'http://www.labgeolivre.ufpr.br/arquivos/ipeadata_04-04-2022-09-10_.csv'
    df_casos = pd.read_csv(tabela, encoding='utf-8', delimiter=',')
    #st.write(casos)
    #st.write(df_casos.head())
    Join = pd.merge(df_BR, df_casos, left_on="SIGLA", right_on="Sigla")

    st.write('A seguir, o mapa mostra a porcentagem de pessoas analfabetas, com 15 anos ou mais, por Unidade de Federação, levantados pelo IBGE no último censo realizado no país.')
    st.subheader('Taxa de analfabetismo por estado brasileiro')

    m = folium.Map(location=[-12.9, -50.4], zoom_start=4)
    bins = list(df_casos['2,014.00'].quantile([0, 0.25, 0.5, 0.75, 1]))
    folium.Choropleth(
        geo_data=df_BR,
        name='Analfabetos',
        data=df_casos,
        columns=['Estado', '2,014.00'],
        key_on='feature.properties.NM_UF',
        fill_color='YlOrRd',
        legend_name='Analfabetos (%) pessoas com 15 anos ou mais',
        bins=bins,
        # labels={'BAIRRO'},
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
            fields=['NM_UF', '2,014.00'],
            aliases=['UF: ', 'Taxa (%):'],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"))
    )
    m.add_child(NIL)
    m.keep_in_front(NIL)
    folium.LayerControl().add_to(m)
    folium_static(m)
    st.write('**OBS:** As informações sobre as taxas de analfabetismo por Unidade de Federação foram obtidas no último censo realizado no país, em 2010.')

    st.write(Join.head())
    casos= df_BR.groupby("NM_UF")[['NM_REGIAO']].count().reset_index()
    m = folium.Map(location=[-12.9, -50.4], zoom_start=4, control_scale=True)
    bins = list(Join['2,014.00'].quantile([0, 0.25, 0.5, 0.75, 1]))
    folium.Choropleth(
        geo_data=Join,
        name='Analfabetos',
        data=casos,
        columns=['NM_REGIAO', '2,014.00'],
        key_on='feature.properties.NM_UF',
        fill_color='YlOrRd',
        legend_name='Analfabetos (%) pessoas com 15 anos ou mais',
        bins=bins,
        # labels={'BAIRRO'},
    ).add_to(m)
    folium.LayerControl().add_to(m)
    folium_static(m)

    st.subheader('Fonte dos dados')
    st.info("""
        \n 🔍 [IPEA - Instituto de Pesquisa Econômica Aplicada](http://www.ipeadata.gov.br/Default.aspx).
        \n 🔍 [IBGE - Instituto Brasileiro de Geografia e Estatística](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html?=&t=acesso-ao-produto).""")



