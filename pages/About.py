import streamlit as st  # Corrected the import alias to 'st' from 'sr'

st.markdown("### About me...")
st.markdown("![Profile Image](https://github.com/MK316/MK-316/raw/main/images/profile-small.jpg)")  # Correct markdown syntax for images
st.caption("I teach phonetics and phonology to English education majors, focusing on advancing digital literacy for today’s evolving classrooms. My work emphasizes student-centered, technology-enhanced learning to equip future teachers with interactive, engaging methods that minimize reliance on commercial applications. Since February 2022, I have been learning foundational Python coding to enhance instructional approaches and am dedicated to developing professional courses for in-service teachers interested in integrating digital tools. I am also exploring coding-based language learning app development.")
st.markdown("\n\n")
st.markdown("- Linguist (Phonetics/Phonology) & educator")
st.markdown("- Github ID: MK316")
st.markdown("- Affiliation: Dept. of English Education, GNU ⛺ [Goto](https://englishedu.gnu.ac.kr)")
st.markdown("- Archives (before 10. 14. 2024) - My digital classroom: [mrkim21.github.io](https://mrkim21.github.io)")

# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
# Display the image
st.image(image_url, caption="\"Be curious, not judgmental.\" — Walt Whitman", use_column_width=True)
