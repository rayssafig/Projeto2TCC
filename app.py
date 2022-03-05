import streamlit as st
from multiapp import MultiApp
from apps import (saude, Home)
from PIL import Image

icon = Image.open("SDG Wheel_PRINT_Transparent.png")
st.set_page_config(layout='wide', page_title='Objetivos de Desenvolvimento Sustentável', page_icon=icon)

#Declaring streamlit containers
header = st.container()
user_input = st.container()
output_graphs = st.container()
author_credits = st.container()


apps = MultiApp()

# Add all your application here

#apps.add_app("Home", home.app)
#apps.add_app("Erradicação da pobreza", timelapse.app)
#apps.add_app("Fome Zero e Agricultura Sustentável", housing.app)
apps.add_app("Home", Home.app)
apps.add_app("Saúde e Bem-Estar", saude.app)


# The main app
apps.run()