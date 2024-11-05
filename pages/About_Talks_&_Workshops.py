import streamlit as st
import requests

image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
st.image(image_url, caption="\"Teaching is one of the best ways to learn.\"", use_column_width=True)

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
    
    # Set up tabs
    tabs = st.tabs(["Archives", "Current", "Additional Content"])

    # Fall 2024 content
    with tabs[0]:
    #    st.subheader("Fall 2024 Courses")
        workshop_url = 'https://github.com/MK316/workshops/blob/main/README.md'
        workshop_content = fetch_github_readme(workshop_url)
        st.markdown(workshop_content, unsafe_allow_html=True)

    # Spring 2024 content
    with tabs[1]:
        st.subheader("Currently scheduled")
       # spring_url = 'https://github.com/MK316/MK-316/blob/main/pages/spring2024.md'
       # spring_content = fetch_github_readme(spring_url)
       # st.markdown(spring_content, unsafe_allow_html=True)
        st.caption("December 2024, TBA")

     # Additional Content tab (optional)
    with tabs[2]:
        st.subheader("Additional Content")
        # Placeholder URL for additional content if needed
        # Uncomment and update the URL if you have content for this tab
        # additional_url = 'https://github.com/MK316/Coding4ET/blob/main/Lessons/Lesson02.md'
        # additional_content = fetch_github_readme(additional_url)
        # st.markdown(additional_content, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

