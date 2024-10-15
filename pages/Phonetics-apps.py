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
        st.markdown("[App 1](https://ipa-practice.streamlit.app/)")
        st.caption("#phonetics #learning")

    with col2:
        st.image("path_to_icon2.png", width=100)
        st.markdown("[App 2](https://your-second-app-url.com)")
        st.caption("#speech #analysis")

    with col3:
        st.image("path_to_icon3.png", width=100)
        st.markdown("[App 3](https://your-third-app-url.com)")
        st.caption("#interactive #training")

phonetics_apps_page()
