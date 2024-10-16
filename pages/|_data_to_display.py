import streamlit as st
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text data for the word cloud
text = "Streamlit is an open-source app framework for Machine Learning and Data Science projects."

# Creating the word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(text)
    return wordcloud

# Streamlit tabs
tab1, tab2, tab3 = st.tabs(["📈 Chart", "🗃 Data", "🌌 Word Cloud"])

# Random data for chart
data = np.random.randn(10, 1)

# Chart tab
tab1.subheader("A tab with a chart")
tab1.line_chart(data)

# Data tab
tab2.subheader("A tab with the data")
tab2.write(data)

# Word cloud tab
tab3.subheader("A tab with a word cloud")
wordcloud = create_wordcloud(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
tab3.pyplot(fig)
