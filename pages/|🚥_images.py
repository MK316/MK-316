import streamlit as st

tab1, tab2, tab3 = st.tabs(["2024 Gallery", "gallery 2", "gallery 3"])

with tab1:
    st.header("2024 Memories")
    st.image("https://github.com/MK316/MK-316/raw/main/images/2410a.png", width=200)
    st.write("01")
    st.image("https://github.com/MK316/MK-316/raw/main/images/2410b.png", width=200)
    st.write("02")
    st.image("https://github.com/MK316/MK-316/raw/main/images/2410c.png", width=200)
    st.write("03")
    st.image("https://github.com/MK316/MK-316/raw/main/images/2409a.png", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
