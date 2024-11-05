import streamlit as st

# Title of the application
st.title("Phonetics Tools")

# Create two tabs: 'Vowel Chart' and 'V-description app'
tab1, tab2 = st.tabs(["Vowel Chart", "V-description app"])

# Define the content of each tab
with tab1:
    st.header("Vowel Chart")
    st.markdown("This tool provides a vowel chart for phonetics practice.")

    # Create a button that opens the vowel chart link in a new tab
    vowel_chart_url = "https://vowelchart.streamlit.app"
    if st.button("Open Vowel Charting"):
        js_code = f"window.open('{vowel_chart_url}');"
        st.components.v1.html(f"<script>{js_code}</script>", height=0, width=0)

    st.caption("This tool provides a vowel chart based on formants (F1, F2).")

with tab2:
    st.header("V-description app")
    st.write("To be updated.")
