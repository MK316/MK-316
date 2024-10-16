import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("Archive Digital Classroom")
    st.write("This page displays the archived digital classroom.")

    # URL of the webpage you want to embed
    url = "https://mrkim21.github.io"
    
    # Embed the webpage using an iframe
    components.iframe(url, height=600, scrolling=True)

if __name__ == "__main__":
    main()
