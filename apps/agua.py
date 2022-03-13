import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

def app():
    global data
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-06.png')
    titl.title('ODS 6: Água potável e saneamento')
    st.subheader('Garantir a disponibilidade e a gestão sustentável da água potável e do saneamento para todos')

    #st.image('https://github.com/rayssafig/Projeto2TCC/tree/master/data/Irai_GIF.gif')
    st.image('C:/Users/rayss/PycharmProjects/Projeto2TCC/apps/Irai_GIF.gif')

    df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
    pr = df.profile_report()

    st_profile_report(pr)
