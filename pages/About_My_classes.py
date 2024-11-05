import streamlit as st
import streamlit.components.v1 as components
import requests

def main():
    st.title('Coding4ET Tutorials')

    tabs = st.tabs(["Fall2024", "Spring2024"])

    # Manual tab content
    with tabs[0]:
        st.subheader("")
        readme_url = 'https://github.com/MK316/MK-316/blob/main/pages/fall2024.md'
        readme_content = fetch_github_readme(readme_url)
        st.markdown(readme_content, unsafe_allow_html=True)

    with tabs[1]:
        st.subheader("")
        readme_url = 'https://github.com/MK316/MK-316/blob/main/pages/spring2024.md'
        readme_content = fetch_github_readme(readme_url)
        st.markdown(readme_content, unsafe_allow_html=True)

    with tabs[2]:
        st.subheader("")
        # readme_url = 'https://github.com/MK316/Coding4ET/blob/main/Lessons/Lesson02.md'
        # readme_content = fetch_github_readme(readme_url)
        # st.markdown(readme_content, unsafe_allow_html=True)

 
