import streamlit as st
import branca
from streamlit_folium import folium_static
import folium


def app():

    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-01.png')
    titl.title('ODS 1: Erradicação da pobreza')
    st.subheader('Erradicar a pobreza em todas as formas e em todos os lugares')

    st.title('Mapas folium')

    page = st.radio(
        "Selecione o tipo do mapa:", ["Single map", "Dual map", "Branca figure"], index=0
    )

    # center on Liberty Bell, add marker
    if page == "Single map":
        m = folium.Map(location=[-25.5, -49.3], zoom_start=10)
        tooltip = "Liberty Bell"
        folium.Marker(
            [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
        ).add_to(m)

    elif page == "Dual map":
        m = folium.plugins.DualMap(location=[39.949610, -75.150282], zoom_start=16)
        tooltip = "Liberty Bell"
        folium.Marker(
            [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
        ).add_to(m)

    elif page == "Branca figure":
        m = branca.element.Figure()
        fm = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
        tooltip = "Liberty Bell"
        folium.Marker(
            [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
        ).add_to(fm)
        m.add_child(fm)

    # call to render Folium map in Streamlit
    folium_static(m)






































































































































































































































