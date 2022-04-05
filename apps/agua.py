import streamlit as st
import geopandas as gpd
from streamlit_folium import folium_static
import folium
import requests, zipfile, io
from pathlib import Path


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
    m = folium.Map(location=[-9.4, -37.3], tiles='Stamen Terrain', zoom_start=9)
    folium.Choropleth(
        geo_data=drenagem,
        name='Percentual',
        fill_color='Reds',
    ).add_to(m)
    folium.LayerControl().add_to(m)
    # Mostrar folium map no streamlit
    folium_static(m)

    #terras = gpd.read_file('https://geo.socioambiental.org/webadaptor2/services/raisg/raisg_tis_d/MapServer/WMSServer?request=GetCapabilities&service=WMS')
    st.subheader('Disponibilidade Hídrica Superficial do Brasil')
    st.write('No cálculo da estimativa da disponibilidade hídrica de águas superficiais no Brasil, foi adotada a vazão de restrição dos reservatórios, '
             'acrescida do incremental da vazão de estiagem (vazão com permanência de 95%) para os trechos regularizados (quando não se dispunha da informação '
             'de vazão de restrição utilizou-se a vazão regularizada pelo sistema de reservatórios com 100% de garantia). Em rios sem regularização, '
             'a disponibilidade foi considerada como apenas a vazão (de estiagem) com permanência de 95%.')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

    url = 'https://metadados.snirh.gov.br/geonetwork/srv/api/records/0c75f8eb-f5c7-4643-9f91-5bf86a09fb63/attachments/SNIRH_DispHidricaSuperficial.zip'
    filename = 'plnvw_ft_disponibilidade_hidrica_trecho.shp'
    r = requests.get(url, stream=True, headers=headers)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    df_pr = gpd.read_file(filename, sep=',')

    m = folium.Map(location=[-12.9, -50.4], zoom_start=4)
    bins = list(df_pr['dispq95'].quantile([0, 0.1, 0.75, 0.9, 0.98, 1]))
    folium.Choropleth(
        geo_data=df_pr,
        name='Casos por bairro',
        #data=casos_por_bairro,
        columns=['BAIRRO', 'CLASSIFICAÇÃO FINAL'],
        key_on='feature.properties.NOME',
        fill_color='Blues',
        legend_name='Casos por bairro',
        bins=bins,
        labels={'BAIRRO'},
        style=folium.vector_layers.path_options(line=True, radius=False, color='Blues')
    ).add_to(m)
    folium.LayerControl().add_to(m)
    folium_static(m)

    m = folium.Map(location=[-3.3, -61.9], tiles=None,
                   zoom_start=4, control_scale=True)

    w = folium.WmsTileLayer(url='https://geo.socioambiental.org/webadaptor2/services/raisg/raisg_tis_d/MapServer/WMSServer?request=GetCapabilities&service=WMS',
                            layers='MODIS_Terra_CorrectedReflectance_TrueColor',
                            version='1.3.0',
                            attr="NASA EOSDIS GIBS"
                            )
    w.add_to(m)
    folium_static(m)

