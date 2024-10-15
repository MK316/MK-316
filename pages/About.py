import streamlit as st  # Corrected the import alias to 'st' from 'sr'
# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
# Display the image
st.image(image_url, caption="\"Every student can learn, just not on the same day, or the same way.\" – George Evans", use_column_width=True)


st.markdown("### ❄️ About me...")
st.markdown("![Profile Image](https://github.com/MK316/MK-316/raw/main/images/profile-small.jpg)")  # Correct markdown syntax for images
st.markdown("\n\n")
st.markdown("- Github ID: MK316")
st.markdown("- Affiliation: Dept. of English Education, GNU ⛺ [Goto](https://englishedu.gnu.ac.kr)")
st.markdown("- My digital classroom: [mrkim21.github.io](https://mrkim21.github.io)")
