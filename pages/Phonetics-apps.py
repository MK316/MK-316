import streamlit as st

def phonetics_apps_page():
    st.title('Phonetics Apps')
    st.write('Applications used to teach Phonetics.')

    # Describing your apps briefly
    st.markdown("""
    Here is a selection of applications designed to enhance phonetics learning through interactive and innovative tools. These apps provide resources and exercises to improve pronunciation, listening skills, and phonetic awareness.
    """)

    # Create columns for each application
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/ipa01.png", width=100)
        if st.button('Launch App 1', key='1'):
            st.markdown("Click here to launch [App 1](https://ipa-practice.streamlit.app/)", unsafe_allow_html=True)
    
    with col2:
        st.image("images/ipa01.png", width=100)
        if st.button('Launch App 2', key='2'):
            st.markdown("Click here to launch [App 2](https://MK-316-Stopwatch.hf.space)", unsafe_allow_html=True)
    
    with col3:
        st.image("images/ipa01.png", width=100)
        if st.button('Launch App 3', key='3'):
            st.markdown("Click here to launch [App 3](https://playsound.streamlit.app/)", unsafe_allow_html=True)

phonetics_apps_page()
