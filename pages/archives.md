# Play audio (as buttons)
import streamlit as st

def phonetics_apps_page():
    st.title('🐾Play sound Apps')
    st.write('Applications used to teach Phonetics.')

    # Describing your apps briefly
    st.markdown("""
    Here is a selection of applications designed to enhance phonetics learning through interactive and innovative tools. These apps provide resources and exercises to improve pronunciation, listening skills, and phonetic awareness.
    """)

    # First row with three columns
    col1, col2, col3 = st.columns(3)  # Define columns for the first row

    with col1:
        st.image("images/button03.png", width=100)
        if st.button('App 2: Playsound', key='2'):
            st.markdown("🌀[App link](https://playsound.streamlit.app/): Upload audio to play; Speed controller", unsafe_allow_html=True)
            st.markdown("2024.10.14")
    
    with col2:
        st.image("images/button03.png", width=100)
        if st.button('App 6: MP3-to-wav', key='6'):
            st.markdown("🌀[App link](https://mk-316-mp3towav.hf.space/): Convert mp3 to wav file", unsafe_allow_html=True)
            st.markdown("2024.10.15")
            
phonetics_apps_page()

# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
# Display the image
st.image(image_url, caption="\"He who knows no foreign languages knows nothing of his own.\" — Johann Wolfgang von Goethe", use_column_width=True)


