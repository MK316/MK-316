import streamlit as st

def phonetics_apps_page():
    st.title('🐾 Play sound Apps')
    st.write('Applications used to teach Phonetics.')

    # Describing the audio-related applications
    st.markdown("""
    Here is a selection of audio-related applications specifically designed to enhance phonetics learning. These tools cater to various needs, such as playing audio files, converting file formats, and utilizing Text-to-Speech technology. They offer interactive exercises to improve pronunciation, develop listening skills, and heighten phonetic awareness, making them invaluable resources for learners and educators alike.
    """)

    # Using tabs for different apps
    tab1, tab2, tab3 = st.tabs(["Play audio", "MP3-to-wav", "Multi-TTS"])

    with tab1:
        st.image("images/button03.png", width=100)
        st.markdown("🌀 [App link](https://playsound.streamlit.app/): Upload audio to play; Speed controller", unsafe_allow_html=True)
        st.markdown("2024.10.14")

    with tab2:
        st.image("images/button03.png", width=100)
        st.markdown("🌀 [App link](https://mk-316-mp3towav.hf.space/): Convert mp3 to wav file", unsafe_allow_html=True)
        st.markdown("2024.10.15")

    with tab3:
        st.image("images/button03.png", width=100)
        st.markdown("🌀 [App link](https://MK-316-MultiTTS.hf.space): Multi-Text-to-Speech application", unsafe_allow_html=True)
        st.markdown("Access the latest in Text-to-Speech technology.")

phonetics_apps_page()

# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
# Display the image
st.image(image_url, caption="\"He who knows no foreign languages knows nothing of his own.\" — Johann Wolfgang von Goethe", use_column_width=True)
