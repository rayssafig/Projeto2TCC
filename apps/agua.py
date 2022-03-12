import streamlit as st


def app():
    global data
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-06.png')
    titl.title('ODS 6: Água potável e saneamento')
    st.subheader('Garantir a disponibilidade e a gestão sustentável da água potável e do saneamento para todos')

    #st.image('C:/Users/rayss/PycharmProjects/Projeto2TCC/data/Irai_GIF.gif')
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.image("C:/Users/rayss/PycharmProjects/Projeto2TCC/data/Irai_GIF.gif")
        st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

    with row1_col2:
        st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
        st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")