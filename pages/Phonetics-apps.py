import streamlit as st

def phonetics_apps_page():
    st.title('Phonetics Apps')
    st.write('Applications used to teach Phonetics.')

    # Describing your apps briefly
    st.markdown("""
    Here is a selection of applications designed to enhance phonetics learning through interactive and innovative tools. These apps provide resources and exercises to improve pronunciation, listening skills, and phonetic awareness.
    """)

    # First row with five columns
    col1, col2, col3= st.columns(3)

    with col1:
        st.image("images/ipa01.png", width=100)
        if st.button('App 1: \nIPA quiz', key='1'):
            st.markdown("[Open the app](https://ipa-practice.streamlit.app/) \n IPA symbols, Quiz, Phonetic description", unsafe_allow_html=True)
    
    with col2:
        st.image("images/ipa01.png", width=100)
        if st.button('App 2: Stopwatch', key='2'):
            st.markdown("Click here to launch [App 2](https://MK-316-Stopwatch.hf.space)", unsafe_allow_html=True)
    
    with col3:
        st.image("images/ipa01.png", width=100)
        if st.button('App 3: Playsound', key='3'):
            st.markdown("Click here to launch [App 3](https://playsound.streamlit.app/)", unsafe_allow_html=True)
    

    # Add some space before the second row
    st.write("\n\n")  # Adjust the number of new lines as needed

    # Second row with three columns
    col6, col7, col8 = st.columns(3)

    with col6:
        st.image("images/ipa01.png", width=100)
        if st.button('App 4: Additional Tool', key='4'):
            st.markdown("Additional details for App 4", unsafe_allow_html=True)

    with col7:
        st.image("images/ipa01.png", width=100)
        if st.button('App 5: Learning Tool', key='5'):
            st.markdown("Additional details for App 5", unsafe_allow_html=True)

    with col8:
        st.image("images/ipa01.png", width=100)
        if st.button('App 6: Practice Tool', key='6'):
            st.markdown("Additional details for App 6", unsafe_allow_html=True)

phonetics_apps_page()
