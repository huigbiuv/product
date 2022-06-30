import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px
#from wordcloud import WordCloud, STOPWORDS
#import matplotlib.pyplot as plt

st.title("Sentiment Analysis of Tweets about US Airlines")
st.sidebar.title("Sentiment Analysis of Tweets about US Airlines")

st.markdown(" This application is a Streamlit app used to analyze the sentiment of the tweets 🐦 about US airlines ✈️ ")
st.sidebar.markdown(" This application is a Streamlit app used to analyze the sentiment of the tweets 🐦 about US airlines ✈️ ")
DATA_URL = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vRffwlmhiARpcl03gaG07TDMbFCbjJOdFpOkscij4-CPIwzNCiQdwC8TsxBjKjN6zV3BUraUDjxUC0p/pub?gid=1245683872&single=true&output=csv")


@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    data['Variant Updated At'] = pd.to_datetime(data['Variant Updated At'])
    return data

data = load_data()

st.sidebar.subheader("Show random tweet")
random_tweet = st.sidebar.radio('Sentiment type', ('positive','negative','neutral'))
st.sidebar.markdown(data.query('airline_sentiment == @random_tweet')[["text"]].sample(n=1).iat[0,0])

st.sidebar.markdown("### Number of tweets by sentiment type")
select = st.sidebar.selectbox('Vizualization type', ['Histogram', 'Pie Chart'], key='1')
sentiment_count = data['airline_sentiment'].value_counts()
sentiment_count = pd.DataFrame({'Sentiment' :sentiment_count.index, 'Tweets' :sentiment_count.values})

if not st.sidebar.checkbox('Hide', True):
    st.markdown("### Number of tweets by Sentiment")
    if select == "Histogram":
        fig = px.bar(sentiment_count, x='Sentiment', y='Tweets', color = 'Tweets', height= 500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)
