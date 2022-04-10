import streamlit as st
from multiapp import MultiApp
from apps import (saude, Home, pobreza, fome, genero, agua, educacao)
from PIL import Image

# Definindo o ícone e titulo da página
icon = Image.open("SDG Wheel_PRINT_Transparent.png")
st.set_page_config(layout='wide', page_title='Objetivos de Desenvolvimento Sustentável', page_icon=icon)

apps = MultiApp()

# Adicionando as aplicações
apps.add_app('Página Inicial', Home.app)
apps.add_app("1 - Erradicação da pobreza", pobreza.app)
apps.add_app("2 - Fome Zero e Agricultura Sustentável", fome.app)
apps.add_app("3 - Saúde e Bem-Estar", saude.app)
apps.add_app("4 - Educação de qualidade", educacao.app)
apps.add_app("5 - Igualdade de Gênero", genero.app)
apps.add_app("6 - Água potável e saneamento", agua.app)

# The main app
apps.run()
