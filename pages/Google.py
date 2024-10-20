import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("Search on Google")
    st.write("Webpage embedding")

    # URL of the webpage you want to embed
    url = "https://google.com"
    
    # Embed the webpage using an iframe
    components.iframe(url, height=600, scrolling=True)

if __name__ == "__main__":
    main()
