from random import randint

import streamlit as st

from streamlit_observable import observable
import leafmap.foliumap as leafmap


def app():

    titl, imga = st.columns((4, 1))
    imga.image('E_SDG_logo_UN_emblem_square_trans_WEB.png')
    titl.title('Mapeando os Indicadores dos Objetivos de Desenvolvimento Sustentável da ONU')
    st.write('Seja bem-vindo a essa aplicação _open-source_, reprodutível, para visualizar dados e mapas relacionados aos Objetivos de Desenvolvimento Sustentpavel (ODS) e seus indicadores.')

    st.markdown("""
        A aplicação tem o objetivo de apresentar diferentes ***dashboards*** para representar os ODS e seus indicadores, através de mapas interativos, gráficos e demais dados oriundos de fontes livres
        e bibliotecas geoespaciais como [folium](https://python-visualization.github.io/folium/modules.html), [geopandas](https://geopandas.org/), [leafmap](https://leafmap.org), [geemap](https://geemap.org), [pydeck](https://deckgl.readthedocs.io), e [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter).""")

    st.info("🚨 **Selecione no menu à esquerda para navegar entre as diferentes aplicações** 🚨 ")

    st.subheader("Introdução")
    st.markdown("""Os Objetivos de Desenvolvimento Sustentável são um apelo global à ação para acabar com a pobreza, proteger o meio ambiente e o clima e garantir que as pessoas, em todos os lugares, possam desfrutar de paz e de prosperidade. 
    """)
    st.write('Totalizam 17 Objetivos de Desenvolvimento Sustentável para atingir a Agenda 2030, apresentados como:')

    imga, titl = st.columns((0.3, 5))
    titl.write('**Erradicação da Pobreza**')
    imga.image('E-WEB-Goal-01.png')

    imga, titl = st.columns((0.3, 5))
    titl.write('**Fome zero e agricultura sustentável**')
    imga.image('E-WEB-Goal-02.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Saúde e Bem-Estar**')
    imga.image('E-WEB-Goal-03.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Educação de Qualidade**')
    imga.image('E-WEB-Goal-04.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Igualdade de gênero**')
    imga.image('E-WEB-Goal-05.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Água potável e saneamento**')
    imga.image('E-WEB-Goal-06.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Energia limpa e acessível**')
    imga.image('E-WEB-Goal-07.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Trabalho decente e crescimento econômico**')
    imga.image('E-WEB-Goal-08.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Indústria, inovação e infraestrutura**')
    imga.image('E-WEB-Goal-09.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Redução das desigualdades**')
    imga.image('E-WEB-Goal-10.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Cidades e comunidades sustentáveis**')
    imga.image('E-WEB-Goal-11.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Consumo e produção responsáveis**')
    imga.image('E-WEB-Goal-12.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Ação contra a mudança global do clima**')
    imga.image('E-WEB-Goal-13.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Vida na água**')
    imga.image('E-WEB-Goal-14.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Vida terrestre**')
    imga.image('E-WEB-Goal-15.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Paz, justiça e instituições eficazes**')
    imga.image('E-WEB-Goal-16.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Parceria e meios de implementação**')
    imga.image('E-WEB-Goal-17.png')

    st.write('O objetivo principal dessa aplicação é apresentar dados que representem os ODS e seus indicadores.')
             
    st.write('Com foco em promover análises geoespaciais, dados espaciais serão utilizados para permitir ao usuário visualizar diferentes recortes geográficos,'
             ' a nível municipal, estadual, nacional e até global.')

    st.info('🧭 Aproveite a experiência e navegue pelas diferentes páginas para visualizar os ODS. 🔍')

    #observers = observable("Tour pelo mundo!",
                           #notebook="@d3/world-tour",
                           #targets=["canvas"],
                           #observe=["name"]
                           #)
#
    #name = observers.get("name")
#
    #st.write(f"Você está vendo o país: *{name}*")

    st.markdown("## Obrigada por utilizar essa aplicação!")
    st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
    btn = st.button("Celebrate!")
    if btn:
        st.balloons()

