import streamlit as st
from multiapp import MultiApp
from apps import (saude)

st.set_page_config(layout="wide")

apps = MultiApp()

# Add all your application here

#apps.add_app("Home", home.app)
#apps.add_app("Erradicação da pobreza", timelapse.app)
#apps.add_app("Fome Zero e Agricultura Sustentável", housing.app)
apps.add_app("Saúde e Bem-Estar", saude.app)


# The main app
apps.run()