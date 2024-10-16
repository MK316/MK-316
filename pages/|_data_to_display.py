import streamlit as st
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# Initialize session state for current tab if not already set
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = 'Chart'

# Creating the word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Function to set the current tab in session state
def set_tab():
    st.session_state.current_tab = st.session_state.tab

# Streamlit tabs
tab_keys = ["📈 Chart", "🗃 Data", "🌌 Word Cloud", "🌐 MK316-digitalclassroom"]
tab1, tab2, tab3, tab4 = st.tabs(tab_keys)

# Set current tab on tab change
for i, tab_key in enumerate(tab_keys):
    if eval(f'tab{i+1}'):
        st.session_state.tab = tab_key
        set_tab()

# Random data for chart
data = np.random.randn(10, 1)

# Display content based on current tab
if st.session_state.current_tab == "📈 Chart":
    tab1.subheader("A tab with a chart")
    tab1.line_chart(data)

elif st.session_state.current_tab == "🗃 Data":
    tab2.subheader("A tab with the data")
    tab2.write(data)

elif st.session_state.current_tab == "🌌 Word Cloud":
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

elif st.session_state.current_tab == "🌐 MK316-digitalclassroom":
    tab4.subheader("MK316-digitalclassroom")
    tab4.write("Below is an embedded webpage:")
    url = "https://mrkim21.github.io"
    components.iframe(url, height=600, scrolling=True)
