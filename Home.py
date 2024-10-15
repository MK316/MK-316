import streamlit as st

# Include custom CSS for Roboto font from Google Fonts
font_url = "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap"
css = f"""
<style>
@import url('{font_url}');

/* Apply the Roboto font globally */
html, body, div, p, span, h1, h2, h3, h4, h5, h6 {{
    font-family: 'Roboto', sans-serif !important;
}}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

st.title("🌾 MK316")
st.markdown("### _Application Gallery_")

# Additional content
st.markdown("""
Welcome to MK316 - your hub for exploring innovative language learning applications powered by Streamlit! Dive into our projects, or explore my digital classroom at [mrkim21.github.io](https://mrkim21.github.io).
""")

st.markdown("""
I'm on a journey to learn coding to develop language apps that are **_customized_** and **_learner-centered_**, 
rather than relying on solutions that don't necessarily fit my students and classroom. 

My goal is to create **_simple_** but **_interactive_** tools that make language learning more engaging and effective. I'm excited to share this process with you as we explore new, impactful ways to teach languages.
""")
st.markdown("Since Oct. 14, 2024")
