import streamlit as st

def phonetics_apps_page():
    st.title('Phonetics Apps')
    st.write('Applications used to teach Phonetics.')

    # Describing your apps briefly
    st.markdown("""
    Here is a selection of applications designed to enhance phonetics learning through interactive and innovative tools. These apps provide resources and exercises to improve pronunciation, listening skills, and phonetic awareness.
    """)

    # First row with three columns
    col1, col2, col3 = st.columns(3)  # Define columns for the first row

    with col1:
        st.image("images/button01.png", width=100)
        if st.button('App 1: \nIPA quiz', key='1'):
            st.markdown("🌀[App link](https://ipa-practice.streamlit.app/): IPA Quiz with phonetic descriptions; Scoring", unsafe_allow_html=True)
            st.markdown("2024.10.14")
    with col2:
        st.image("images/button03.png", width=100)
        if st.button('App 2: Playsound', key='2'):
            st.markdown("🌀[App link](https://playsound.streamlit.app/): Upload audio to play; Speed controller", unsafe_allow_html=True)
            st.markdown("2024.10.14")
    
    with col3:
        st.image("images/button01.png", width=100)
        if st.button('App 3: Distinctive features', key='3'):
            st.markdown("🌀[App link](https://mk-316-featureapp01.hf.space/): Phonology, Sound grouping from distinctive features", unsafe_allow_html=True)
            st.markdown("2024.10.15")
    
    # Add some space before the second row
    st.write("\n\n")

    # Second row with three columns
    col4, col5, col6 = st.columns(3)  # Correct typo here

    with col4:
        st.image("images/button01.png", width=100)
        if st.button('App 4: List sounds', key='4'):
            st.markdown("🌀[App link](https://mk-316-ipaselect.hf.space/): Display sounds from phonetic descriptions", unsafe_allow_html=True)
            st.markdown("2024.10.14")

    with col5:
        st.image("images/button01.png", width=100)
        if st.button('App 5: Feature Quiz', key='5'):
            st.markdown("🌀[App link](https://mk-316-feature-practice.hf.space/): Phonology, Distinctive feature quiz", unsafe_allow_html=True)
            st.markdown("2024.10.14")

    with col6:
        st.image("images/button03.png", width=100)
        if st.button('App 6: MP3-to-wav', key='6'):
            st.markdown("🌀[App link](https://mk-316-mp3towav.hf.space/): Convert mp3 to wav file", unsafe_allow_html=True)
            st.markdown("2024.10.15")

phonetics_apps_page()
