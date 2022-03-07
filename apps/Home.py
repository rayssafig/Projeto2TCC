import streamlit as st
import leafmap.foliumap as leafmap
#Declaring streamlit containers
#header = st.container()

#with header:


def app():
#    st.title("Streamlit for Geospatial Applications")

    titl, imga = st.columns((4, 1))
    imga.image('E_SDG_logo_UN_emblem_square_trans_WEB.png')
    titl.title('Objetivos de Desenvolvimento Sustentável da ONU')
    st.write('***Uma aplicação open-source, reprodutível, para gerenciar e publicar dados e mapas relacionados aos Objetivos de Desenvolvimento Sustentpavel (ODS).')

    st.markdown(
        """
        Essa aplicação com várias páginas tem o objetivo de apresentar diferentes aplicações para representar os ODS e seus indicadores, através de mapas interativos, gráficos e demais dados oriundos de fontes livres para montar o dashboard
        como [leafmap](https://leafmap.org), [geemap](https://geemap.org), [pydeck](https://deckgl.readthedocs.io), e [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter).
    
        """
    )

    st.info("Selecione no menu à esquerda para navegar entre os diferentes ODS")

    st.subheader("Timelapse of Satellite Imagery")
    st.markdown(
        """
        The following timelapse animations were created using the Timelapse web app. Click `Create Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
    """
    )

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
        st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

    with row1_col2:
        st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
        st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")