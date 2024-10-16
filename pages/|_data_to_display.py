import streamlit as st
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# Creating the word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Streamlit tabs
tabs = st.tabs(["📈 Chart", "🗃 Data", "🌌 Word Cloud", "🌐 MK316-digitalclassroom"])

# Random data for chart
data = np.random.randn(10, 1)

# Chart tab
with tabs[0]:
    st.subheader("A tab with a chart")
    st.line_chart(data)

# Data tab
with tabs[1]:
    st.subheader("A tab with the data")
    st.write(data)

# Word cloud tab
with tabs[2]:
    st.subheader("A tab with a word cloud")
    st.markdown("Please enter some text to generate a word cloud. [sample text](https://raw.githubusercontent.com/MK316/MK-316/refs/heads/main/data/sampletext.txt)")
    user_input = st.text_input("Enter text to create a word cloud:")
    generate_button = st.button("Generate Word Cloud")

    if generate_button and user_input:  # Generate only when the button is clicked
        wordcloud = create_wordcloud(user_input)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

# Webpage embedding tab - now embedding a YouTube video
with tabs[3]:
    st.subheader("MK316-digitalclassroom")
    st.write("Below is an embedded video from YouTube: Coding basics")
    video_url = "https://youtu.be/uigxMFBR0Wg"  # Replace INSERT_VIDEO_ID_HERE with your actual YouTube video ID
    st.video(video_url)
