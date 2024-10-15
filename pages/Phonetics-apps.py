import streamlit as st

def phonetics_apps_page():
    st.title('Phonetics Apps')
    st.write('Applications used to teach Phonetics.')

    # Describing your apps briefly
    st.markdown("""
    Here is a selection of applications designed to enhance phonetics learning through interactive and innovative tools. These apps provide resources and exercises to improve pronunciation, listening skills, and phonetic awareness.
    """)

    # Create columns for each application
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image("images/ipa01.png", width=100)
        if st.button('App 1: IPA quiz', key='1'):
            st.markdown("[Open the app](https://ipa-practice.streamlit.app/) \n IPA symbols, Quiz, Phonetic description", unsafe_allow_html=True)
    with col2:
        st.image("images/ipa01.png", width=100)
        if st.button('App 2: Stopwatch', key='2'):
            st.markdown("Click here to launch [App 2](https://MK-316-Stopwatch.hf.space)", unsafe_allow_html=True)
    
    with col3:
        st.image("images/ipa01.png", width=100)
        if st.button('App 3: Playsound', key='3'):
            st.markdown("Click here to launch [App 3](https://playsound.streamlit.app/)", unsafe_allow_html=True)
            
    with col4:
        st.image("images/ipa01.png", width=100)
        if st.button('Launch App 4', key='4'):
            st.markdown("Click here to launch [App 2](https://MK-316-Stopwatch.hf.space)", unsafe_allow_html=True)
    
    with col5:
        st.image("images/ipa01.png", width=100)
        if st.button('Launch App 5', key='5'):
            st.markdown("Click here to launch [App 3](https://playsound.streamlit.app/)", unsafe_allow_html=True)

phonetics_apps_page()
