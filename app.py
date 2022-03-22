import streamlit as st
from multiapp import MultiApp
from apps import (saude, Home, pobreza, fome, agua)
from PIL import Image

#Definindo o ícone e titulo da página
icon = Image.open("SDG Wheel_PRINT_Transparent.png")
st.set_page_config(layout='wide', page_title='Objetivos de Desenvolvimento Sustentável', page_icon=icon)

apps = MultiApp()

# Adicionando as aplicações
apps.add_app("Página Inicial", Home.app)
apps.add_app("Erradicação da pobreza", pobreza.app)
apps.add_app("Fome Zero e Agricultura Sustentável", fome.app)
apps.add_app("Saúde e Bem-Estar", saude.app)
apps.add_app("Água potável e saneamento", agua.app)

# The main app
apps.run()