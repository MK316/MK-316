import streamlit as st  # Corrected the import alias to 'st' from 'sr'

st.markdown("### About me...")
st.markdown("![Profile Image](https://github.com/MK316/MK-316/raw/main/images/profile-small.jpg)")  # Correct markdown syntax for images
st.markdown("\n\n")
st.markdown("- Github ID: MK316")
st.markdown("- Affiliation: Dept. of English Education, GNU ⛺ [Goto](https://englishedu.gnu.ac.kr)")
st.markdown("- Archives - My digital classroom: [mrkim21.github.io](https://mrkim21.github.io)")

# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
# Display the image
st.image(image_url, caption="\"Be curious, not judgmental.\" — Walt Whitman", use_column_width=True)
