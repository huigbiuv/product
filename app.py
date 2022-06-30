import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px
#from wordcloud import WordCloud, STOPWORDS
#import matplotlib.pyplot as plt

st.title("Inventory product analysis")
st.sidebar.title("Inventory product analysis")

st.markdown(" This application is a Streamlit app used to analyze the inventory peroduct 🐦  ")
st.sidebar.markdown(" This application is a Streamlit app used to analyze the inventory peroduct 🐦 ")

DATA_URL = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vRffwlmhiARpcl03gaG07TDMbFCbjJOdFpOkscij4-CPIwzNCiQdwC8TsxBjKjN6zV3BUraUDjxUC0p/pub?gid=1245683872&single=true&output=csv")
@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    #data['Variant Updated At'] = pd.to_datetime(data['Variant Updated At'])
    return data

data = load_data()

st.sidebar.checkbox("Show Analysis by product", True, key=1)
select = st.sidebar.selectbox('Select a product',df['Title'])

#get the state selected in the selectbox
state_data = df[df['Title'] == select]
#select_status = st.sidebar.radio("product status", ('Confirmed','Active', 'Recovered', 'Deceased'))
st.bar_chart(center_info_data['Title'])
