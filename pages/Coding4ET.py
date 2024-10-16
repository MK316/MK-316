import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('Coding4ET Tutorials')

    # Define the tabs
    tab_manual, tab_lesson1, tab_lesson2, tab_lesson3, tab_lesson4, tab_lesson5 = st.tabs(
        ["Manual", "Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"]
    )

    # Content for Manual, Lesson1, Lesson2, Lesson4, Lesson5
    tab_manual.write("To be updated.")
    tab_lesson1.write("To be updated.")
    tab_lesson2.write("To be updated.")
    tab_lesson4.write("To be updated.")
    tab_lesson5.write("To be updated.")

    # Special handling for Lesson 3
    with tab_lesson3:
        st.subheader("Lesson 3 Videos")
        # Define video URLs
        tutorial_links = {
            'Lesson 3.1': 'https://www.youtube.com/embed/link_for_lesson_3_1',
            'Lesson 3.2': 'https://www.youtube.com/embed/link_for_lesson_3_2',
            'Lesson 3.3': 'https://www.youtube.com/embed/link_for_lesson_3_3',
            'Lesson 3.4': 'https://www.youtube.com/embed/link_for_lesson_3_4'
        }

        # Create a placeholder for the video
        video_placeholder = st.empty()
        
        # Buttons for Lesson 3
        if st.button('Lesson 3.1'):
            update_video(video_placeholder, tutorial_links['Lesson 3.1'])
        if st.button('Lesson 3.2'):
            update_video(video_placeholder, tutorial_links['Lesson 3.2'])
        if st.button('Lesson 3.3'):
            update_video(video_placeholder, tutorial_links['Lesson 3.3'])
        if st.button('Lesson 3.4'):
            update_video(video_placeholder, tutorial_links['Lesson 3.4'])

def update_video(placeholder, video_url):
    """Update the existing placeholder with a new video URL."""
    placeholder.html(
        f"<iframe width='400' height='300' src='{video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        height=300
    )

if __name__ == "__main__":
    main()
