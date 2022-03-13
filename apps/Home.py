import streamlit as st
import leafmap.foliumap as leafmap


def app():
#    st.title("Streamlit for Geospatial Applications")

    titl, imga = st.columns((4, 1))
    imga.image('E_SDG_logo_UN_emblem_square_trans_WEB.png')
    titl.title('Objetivos de Desenvolvimento Sustentável da ONU')
    st.write('Seja bem-vindo a essa aplicação open-source, reprodutível, para gerenciar e publicar dados e mapas relacionados aos Objetivos de Desenvolvimento Sustentpavel (ODS).')

    st.markdown(
        """
        A aplicação tem o objetivo de apresentar diferentes ***dashboards*** para representar os ODS e seus indicadores, através de mapas interativos, gráficos e demais dados oriundos de fontes livres
        como [leafmap](https://leafmap.org), [geemap](https://geemap.org), [pydeck](https://deckgl.readthedocs.io), e [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter).
    
        """
    )

    st.info("**Selecione no menu à esquerda para navegar entre os diferentes ODS**")

    st.subheader("Introdução")
    st.markdown("""Os Objetivos de Desenvolvimento Sustentável são um apelo global à ação para acabar com a pobreza, proteger o meio ambiente e o clima e garantir que as pessoas, em todos os lugares, possam desfrutar de paz e de prosperidade. 
    """)
    st.write('Totalizam 17 Objetivos de Desenvolvimento Sustentável para atingir a Agenda 2030, nomeados como:')

    imga, titl = st.columns((0.3, 3))
    titl.write('Erradicação da Pobreza')
    imga.image('C:/Users/rayss/PycharmProjects/Projeto2TCC/logos/E-WEB-Goal-01.png')

