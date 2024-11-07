import streamlit as st
import requests

# Function to fetch and display GitHub Markdown content
def fetch_github_readme(url):
    # Convert GitHub page URL to raw content URL
    raw_url = url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to load content from GitHub."

def main():
    st.title('About me...')

    # Set up tabs
    tabs = st.tabs(["About", "Publications", "Academic services", "Additional Content"])

    # Fall 2024 content
    with tabs[0]:
        st.markdown("![Profile Image](https://github.com/MK316/MK-316/raw/main/images/profile-small.jpg)")
        st.caption("I teach phonetics and phonology to English education majors, focusing on advancing digital literacy for today’s evolving classrooms. My work emphasizes student-centered, technology-enhanced learning to equip future teachers with interactive, engaging methods that minimize reliance on commercial applications. Since February 2022, I have been learning foundational Python coding to enhance instructional approaches and am dedicated to developing professional courses for in-service teachers interested in integrating digital tools. I am also exploring coding-based language learning app development. Welcome aboard!")
        st.markdown("\n\n")
        st.markdown("💧 Linguist (Phonetics/Phonology) & educator")
        st.markdown(":octocat: Github ID: MK316")
        st.markdown("💧 Affiliation: Dept. of English Education, GNU ⛺ [Goto](https://englishedu.gnu.ac.kr)")
        st.markdown("💧 Archives (before 10. 14. 2024) - My digital classroom: [mrkim21.github.io](https://mrkim21.github.io)")

        # URL to the raw image on GitHub
        image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
        # Display the image
        st.image(image_url, caption="\"Be curious, not judgmental.\" — Walt Whitman", use_column_width=True)

    # Publications
    with tabs[1]:
        # URL to the raw image on GitHub
        image_url = "https://github.com/MK316/MK316.github.io/raw/main/images/KeywordCloud_231129.png"
        # Display the image
        st.image(image_url, caption="Research keywords", use_column_width=True)
        spring_url = 'https://github.com/MK316/MK316.github.io/blob/main/res/publications.md'
        spring_content = fetch_github_readme(spring_url)
        st.markdown(spring_content, unsafe_allow_html=True)

    # Academic services
    with tabs[2]:
        url = 'https://github.com/MK316/MK-316/blob/main/pages/academicservices.md'
        additional_content = fetch_github_readme(url)
        st.markdown(additional_content, unsafe_allow_html=True)

    # Additional Content tab (optional)
    with tabs[3]:
        st.subheader("Additional Content")
        # Placeholder URL for additional content if needed
        # Uncomment and update the URL if you have content for this tab
        # additional_url = 'https://github.com/MK316/Coding4ET/blob/main/Lessons/Lesson02.md'
        # additional_content = fetch_github_readme(additional_url)
        # st.markdown(additional_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
