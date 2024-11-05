import streamlit as st
import requests

# Function to fetch and display GitHub Markdown content
def display_github_markdown(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        st.markdown(content, unsafe_allow_html=True)
    else:
        st.error("Failed to load content. Please check the URL.")

# URLs for the GitHub Markdown files
fall_url = "https://github.com/MK316/F2024/blob/main/README.md"
spring_url = "https://raw.githubusercontent.com/username/repository/branch/path/to/Spring2024.md"

# Set up tabs in the Streamlit app
tab1, tab2 = st.tabs(["Fall2024", "Spring2024"])

with tab1:
    st.header("Fall 2024 Information")
    display_github_markdown(fall_url)

with tab2:
    st.header("Spring 2024 Information")
    display_github_markdown(spring_url)
