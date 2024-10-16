import streamlit as st
import streamlit.components.v1 as components
import requests

def main():
    st.title('Coding4ET Tutorials')

    tabs = st.tabs(["Manual", "Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"])

    # Manual tab content
    with tabs[0]:
        st.subheader("Manual")
        readme_url = 'https://github.com/MK316/Coding4ET/blob/main/README.md'
        readme_content = fetch_github_readme(readme_url)
        st.markdown(readme_content, unsafe_allow_html=True)

    # Static content for other tabs
    for i, tab in enumerate(tabs):
        if i > 0:
            with tab:
                if i == 3:  # Special handling for Lesson 3
                    handle_lesson_3_videos()
                else:
                    st.write("To be updated.")

def handle_lesson_3_videos():
    st.subheader("Lesson 3 Videos")
    video_links = {
        'Lesson 3.1': 'https://www.youtube.com/embed/uigxMFBR0Wg',
        'Lesson 3.2': 'https://www.youtube.com/embed/gPIe1Tgie1Q',
        'Lesson 3.3': 'https://www.youtube.com/embed/ofhRZ6k3Ryw',
        'Lesson 3.4': 'https://www.youtube.com/embed/vSsClackic4'
    }
    for lesson in video_links:
        if st.button(lesson):
            components.html(get_iframe(video_links[lesson]), height=300)

def get_iframe(video_url):
    return f"<iframe width='400' height='300' src='{video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"

def fetch_github_readme(url):
    # Assuming the README is public and raw content is accessible
    # This is a simplified example and may need adjustments based on actual content access policies
    response = requests.get(url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/'))
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to load README. [View on GitHub](" + url + ")"

if __name__ == "__main__":
    main()
