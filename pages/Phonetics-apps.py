import streamlit as st

def phonetics_apps_page():
    st.title('Phonetics Apps')
    st.write('Applications used to teach Phonetics.')

    # Describing your apps briefly
    st.markdown("""
    Here is a selection of applications designed to enhance phonetics learning through interactive and innovative tools. These apps provide resources and exercises to improve pronunciation, listening skills, and phonetic awareness.
    """)

    # Create columns for each application
    # Adjust the number of columns based on your needs
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("path_to_icon1.png", width=100)  # Path to your app icon
        st.write("App 1")
        st.caption("#phonetics #learning")

    with col2:
        st.image("path_to_icon2.png", width=100)  # Path to your app icon
        st.write("App 2")
        st.caption("#speech #analysis")

    with col3:
        st.image("path_to_icon3.png", width=100)  # Path to your app icon
        st.write("App 3")
        st.caption("#interactive #training")

    # You can add more apps in new rows by creating new columns instances
    # Example: col4, col5, col6 = st.columns(3)

# Call the function to display the page
phonetics_apps_page()
