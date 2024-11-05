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
    st.markdown("[Vowel charting](https://vowelchart.streamlit.app)")
    st.caption("This tool provides a vowel chart based on formants (F1, F2).")

with tab2:
    st.header("V-description app")
    st.write("To be updated.")
