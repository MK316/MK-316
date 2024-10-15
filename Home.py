import streamlit as st


# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"

# Display the image
st.image(image_url, caption="\"Wannna really learn coding? Give teaching a go!\"", use_column_width=True)

st.image("https://github.com/MK316/MK-316/raw/main/images/mk316.png", caption="MK316 logo", width = 10, use_column_width=True)
st.markdown("### _Welcome to my application gallery_")

# Additional content
st.markdown("This will be a digital app gallery for exploring innovative language learning applications powered by Streamlit! (Started on Oct. 14) The gallery is still under preparation, but in the meantime, feel free to explore my digital classroom at [mrkim21.github.io](https://mrkim21.github.io).")

st.markdown("""
I'm on a journey to learn coding to develop language apps that are **_customized_** and **_learner-centered_**, 
rather than relying on solutions that don't necessarily fit my students and classroom. 

My goal is to create **_simple_** but **_interactive_** tools that make language learning more engaging and effective. I'm excited to share this process with you as we explore new, impactful ways to teach languages.
""")
st.markdown("Since Oct. 14, 2024")
