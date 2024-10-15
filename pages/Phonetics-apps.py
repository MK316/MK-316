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
    
    with col2:
        st.image("images/button03.png", width=100)
        if st.button('App 2: Playsound', key='2'):
            st.markdown("🌀[App link](https://playsound.streamlit.app/): Upload audio to play; Speed controller", unsafe_allow_html=True)
    
    with col3:
        st.image("images/button01.png", width=100)
        if st.button('App 3: Distinctive features', key='3'):
            st.markdown("🌀[App link](https://mk-316-featureapp01.hf.space/): Phonology, Sound grouping from distinctive features", unsafe_allow_html=True)
    
    # Add some space before the second row
    st.write("\n\n")

    # Second row with three columns
    col4, col5, col6 = st.columns(3)  # Correct typo here

    with col4:
        st.image
