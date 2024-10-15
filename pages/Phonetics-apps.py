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
        # Linking directly on the image
        st.markdown(f'<a href="https://ipa-practice.streamlit.app/" target="_blank"><img src="images/ipa01.png" width="100"></a>', unsafe_allow_html=True)
        st.markdown("[App 1](https://ipa-practice.streamlit.app/)")
        st.caption("#phonetics #learning")

    with col2:
        st.markdown(f'<a href="https://your-second-app-url.com" target="_blank"><img src="path_to_icon2.png" width="100"></a>', unsafe_allow_html=True)
        st.markdown("[App 2](https://your-second-app-url.com)")
        st.caption("#speech #analysis")

    with col3:
        st.markdown(f'<a href="https://your-third-app-url.com" target="_blank"><img src="path_to_icon3.png" width="100"></a>', unsafe_allow_html=True)
        st.markdown("[App 3](https://your-third-app-url.com)")
        st.caption("#interactive #training")

phonetics_apps_page()
