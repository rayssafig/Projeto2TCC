import pandas as pd
import streamlit as st
import geopandas as gpd
import requests
import xmltodict
import urllib
import json

import matplotlib.pyplot as plt
import codecs


def app():
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-05.png')
    titl.title('ODS 5: Igualdade de Gênero')
    st.subheader('Alcançar a igualdade de gênero e empoderar todas as mulheres e meninas')
    st.write('Os dados utilizados para mapear esse ODS são proveninentes de um Atlas geográfico para o estado do Paraná, desenvolvido pela Engenheira Cartógrafa e Agrimensora [Janiny Zanda](http://lattes.cnpq.br/2154838790427332), que foi desenvolvido como '    
            '***"resultado de um Projeto de Conclusão de Curso de Engenharia Cartográfica e de Agrimensura da Universidade Federal do Paraná.'
            ' O Objetivo do projeto é apresentar a utilização da cartografia para monitoramento dos indicadores referentes ao Objetivo de Desenvolvimento Sustentável da ONU número 5 : Igualdade de Gênero.***"')
    st.info('Você pode acessar o Atlas ODS 5 sobre Igualdade de Gênero através do link:'
             '\n [Atlas ODS 5](http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html)')

    page = urllib.request.urlopen("http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html").read()
    #st.write(page)
    page = urllib.request.urlopen("http://www.labgeolivre.ufpr.br/AtlasODSGenero/Meta51/Meta51.html").read()
    #st.write(page)
    url = "http://www.labgeolivre.ufpr.br/AtlasODSGenero/sites.xml"
    response = requests.get(url)
    data = xmltodict.parse(response.content)

    with st.expander('Saber mais sobre os Indicadores do Objetivo 5:'):
        st.write('**5.1** Acabar com todas as formas de discriminação contra todas as mulheres e meninas em toda parte')
        st.write('**5.2** Eliminar todas as formas de violência contra todas as mulheres e meninas nas esferas públicas e privadas, incluindo o tráfico e exploração sexual e de outros tipos')
        st.write('**5.3** Eliminar todas as práticas nocivas, como os casamentos prematuros, forçados e de crianças e mutilações genitais femininas')
        st.write('**5.4** Reconhecer e valorizar o trabalho de assistência e doméstico não remunerado, por meio da disponibilização de serviços públicos, infraestrutura e políticas de proteção social, bem como a promoção da responsabilidade compartilhada dentro do lar e da família, conforme os contextos nacionais')
        st.write('**5.5** Garantir a participação plena e efetiva das mulheres e a igualdade de oportunidades para a liderança em todos os níveis de tomada de decisão na vida política, econômica e pública')
        st.write('**5.6** Assegurar o acesso universal à saúde sexual e reprodutiva e os direitos reprodutivos, como acordado em conformidade com o Programa de Ação da Conferência Internacional sobre População e Desenvolvimento e com a Plataforma de Ação de Pequim e os documentos resultantes de suas conferências de revisão')
        st.write('**5.a** Empreender reformas para dar às mulheres direitos iguais aos recursos econômicos, bem como o acesso a propriedade e controle sobre a terra e outras formas de propriedade, serviços financeiros, herança e os recursos naturais, de acordo com as leis nacionais')
        st.write('**5.b** Aumentar o uso de tecnologias de base, em particular as tecnologias de informação e comunicação, para promover o empoderamento das mulheres')
        st.write('**5.c** Adotar e fortalecer políticas sólidas e legislação aplicável para a promoção da igualdade de gênero e o empoderamento de todas as mulheres e meninas, em todos os níveis')

    st.subheader('Meta 5.1 - Acabar com todas as formas de discriminação contra todas as mulheres e meninas em toda partes')
    st.image('https://media.giphy.com/media/YltbAVJcJlXi6liB0d/giphy.gif', width=600)
    st.write('**OBS:** Para visualizar os mapas, acesse [Atlas ODS 5](http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html).')

    st.subheader('Meta 5.2 - Eliminar todas as formas de violência contra todas as mulheres e meninas nas esferas públicas e privadas, incluindo o tráfico e exploração sexual e de outros tipos')
    st.image('https://media.giphy.com/media/mrdtLiXzr69c9fSbKT/giphy.gif', width=600)
    st.write(
        '**OBS:** Para visualizar os mapas, acesse [Atlas ODS 5](http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html).')

    st.subheader('Meta 5.3 - Eliminar todas as práticas nocivas, como os casamentos prematuros, forçados e de crianças e mutilações genitais femininas')
    st.image('https://media.giphy.com/media/ZpCODSs6svxu7J6UN8/giphy.gif', width=600)
    st.write(
        '**OBS:** Para visualizar os mapas, acesse [Atlas ODS 5](http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html).')

    st.subheader('Meta 5.5 - Garantir a participação plena e efetiva das mulheres e a igualdade de oportunidades para a liderança em todos os níveis de tomada de decisão na vida política, econômica e pública')
    st.image('https://media.giphy.com/media/MQaVdZ2BYtSwBSjgBp/giphy.gif', width=600)
    st.write(
        '**OBS:** Para visualizar os mapas, acesse [Atlas ODS 5](http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html).')

    st.subheader('Meta 5.6 - Assegurar o acesso universal à saúde sexual e reprodutiva e os direitos reprodutivos, como acordado em conformidade com o Programa de Ação da Conferência Internacional sobre População e Desenvolvimento e com a Plataforma de Ação de Pequim e os documentos resultantes de suas conferências de revisão')
    st.image('https://media.giphy.com/media/fZYEVjVaH4UiM77TNQ/giphy.gif', width=600)
    st.write(
        '**OBS:** Para visualizar os mapas, acesse [Atlas ODS 5](http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html).')

    st.subheader('Meta 5.a - Realizar reformas para dar às mulheres direitos iguais aos recursos econômicos, bem como o acesso a propriedade e controle sobre a terra e outras formas de propriedade, serviços financeiros, herança e os recursos naturais, de acordo com as leis nacionais')
    st.image('https://media.giphy.com/media/VoKcsxJP7j4hXYFx0o/giphy.gif', width=600)
    st.write(
        '**OBS:** Para visualizar os mapas, acesse [Atlas ODS 5](http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html).')

    st.subheader('Meta 5.c - Adotar e fortalecer políticas sólidas e legislação aplicável para a promoção da igualdade de gênero e o empoderamento de todas as mulheres e meninas em todos os níveis')
    st.image('https://media.giphy.com/media/ALeNCDdG1hOktEigr7/giphy.gif', width=600)
    st.write(
        '**OBS:** Para visualizar os mapas, acesse [Atlas ODS 5](http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html).')

    st.subheader('Fonte dos dados:')
    st.info("""
        \n 🔍 Atlas ODS 5 - Igualdade de Gênero: [Atlas ODS 5](http://www.labgeolivre.ufpr.br/AtlasODSGenero/index.html).""")


