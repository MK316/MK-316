import streamlit as st

# Title of the application
st.title("Phonetics Tools")

# Create two tabs: 'Vowel Chart' and 'V-description app'
tab1, tab2 = st.tabs(["Vowel Chart", "V-description app"])

# Define the content of each tab
with tab1:
    st.header("Vowel Chart")
    # Display an embedded app using an iframe
    st.markdown("This tool provides a vowel chart for phonetics practice.")
    
    # Replace 'YOUR_APP_URL' with your actual Streamlit app URL for the vowel chart
    YOUR_APP_URL = "https://vowelchart.streamlit.app"
    
    # Use an iframe to embed the app in the tab
    st.components.v1.iframe(YOUR_APP_URL, height=600, width=800)

with tab2:
    st.header("V-description app")
    st.write("To be updated.")
