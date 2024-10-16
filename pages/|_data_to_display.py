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
tab1, tab2, tab3, tab4 = st.tabs(["📈 Chart", "🗃 Data", "🌌 Word Cloud", "🌐 Embed Web"])

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
tab3.markdown("Please enter some text to generate a word cloud. [sample text](https://raw.githubusercontent.com/MK316/MK-316/refs/heads/main/data/sampletext.txt)")
user_input = tab3.text_input("Enter text to create a word cloud:")
generate_button = tab3.button("Generate Word Cloud")

if generate_button and user_input:  # Generate only when the button is clicked
    wordcloud = create_wordcloud(user_input)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    tab3.pyplot(fig)

# Webpage embedding tab
tab4.subheader("Embedded Webpage")
tab4.write("Below is an embedded webpage:")
# URL of the webpage you want to embed
url = "https://padlet.com/mirankim316/message"
# Embed the webpage using an iframe
components.iframe(url, height=400, scrolling=True)
