import streamlit as st

def tce_apps_page():
    st.title('TCE Prep')
    st.write('Applications for TCE preparing students.')

    # Describing your apps briefly
    st.markdown("""
    This page features applications designed to prepare users for Teacher Certificate Exams. The tools offer resources to help their preparation.
    """)

    # Define a single column
    col1, = st.columns(1)  # Note the comma to unpack the column from the list

    with col1:
        st.image("images/TCE.png", width=100)
        if st.button('App 1: TCE exam search', key='1'):
            st.markdown("🌀[App link](https://mk316-TCE.hf.space/): Searchable exam questions in phonetics & phonology", unsafe_allow_html=True)
            st.markdown("2024.02.05")

# Call the function to generate the page content first
tce_apps_page()

# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
# Display the image, now it will appear after everything else
st.image(image_url, caption="\"Teachers have three loves: love of learning, love of learners, and the love of bringing the first two loves together.\" — Scott Hayden", use_column_width=True)
