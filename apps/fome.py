import pandas as pd
import streamlit as st
import json

import csv
import gzip
import io
import json
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen


def app():

    global data
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-02.png')
    titl.title('ODS 2: Fome zero e agricultura sustentável')
    st.subheader('Erradicar a fome, alcançar a segurança alimentar, '
                 'melhorar a nutrição e promover a agricultura sustentável')





