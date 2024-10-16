import streamlit as st
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
tab3.write("Please enter some text to generate a word cloud.")
# Move the user input here to appear below the instruction
user_input = tab3.text_input("Enter text to create a word cloud:")

if user_input:  # Check if there is user input before generating the word cloud
    wordcloud = create_wordcloud(user_input)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    tab3.pyplot(fig)
