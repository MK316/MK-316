import streamlit as st

def class_apps_page():
    st.title('🌱 Classroom management')
    st.write('Applications used in my classroom.')

    # Describing your apps briefly
    st.markdown("""
    This page features a collection of simple applications tailored for class management. These tools are designed to streamline classroom processes, enhance organization, and facilitate smooth communication between educators and students. By integrating these applications, educators can efficiently manage their classes and improve overall classroom dynamics.
    """)


    # First row with three columns
    col1, col2, col3 = st.columns(3)  # Define columns for the first row

    with col1:
        st.image("images/qr.png", width=100)
        if st.button('App 1: QR Code', key='1'):
            st.markdown("🌀[App link](https://mk-316-qrcode.hf.space/): QR code generator", unsafe_allow_html=True)
            st.markdown("2024.10.14")
    with col2:
        st.image("images/stopwatch.png", width=100)
        if st.button('App 2: Stopwatch', key='2'):
            st.markdown("🌀[App link](https://mk-316-Stopwatch.hf.space/): Stopwatch with current time", unsafe_allow_html=True)
            st.markdown("2024.10.14")
    
    with col3:
        st.image("images/grouping.png", width=100)
        if st.button('App 3: Grouping', key='3'):
            st.markdown("🌀[App link](https://mk-316-grouping.hf.space/): Group students for activities; roster", unsafe_allow_html=True)
            st.markdown("2024.1.24")
    
    # Add some space before the second row
    st.write("\n\n")

    # Second row with three columns
    col4, col5, col6 = st.columns(3)  # Correct typo here

    with col4:
        st.image("images/button03.png", width=100)
        if st.button('App 4: Recorder', key='4'):
            st.markdown("🌀[App link](https://mk-316-recorder.hf.space/): Recording from your device", unsafe_allow_html=True)
            st.markdown("2024.02.28")

    with col5:
        st.image("images/button03.png", width=100)
        if st.button('App 5: TTS app', key='5'):
            st.markdown("🌀[App link](https://mk-316-ttsapp.hf.space/): Basic Text-to-Speech", unsafe_allow_html=True)
            st.markdown("2024.1.20")

    with col6:
        st.image("images/wordcloud.png", width=100)
        if st.button('App 6: Wordcloud', key='6'):
            st.markdown("🌀[App link](https://mk-316-wordcloud.hf.space/): Generate a simple wordcloud image from your text", unsafe_allow_html=True)
            st.markdown("2024.04.14")

class_apps_page()

# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
# Display the image
st.image(image_url, caption="\"Good classroom management doesn’t just happen; it’s a skill you cultivate. The art of teaching is the art of assisting discovery.\" — Mark Van Doren", use_column_width=True)

