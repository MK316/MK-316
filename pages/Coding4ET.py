import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('Coding4ET Tutorials')

    # Define video URLs
    tutorial_links = {
        'Lesson 3.1': 'https://www.youtube.com/embed/link_for_lesson_3_1',
        'Lesson 3.2': 'https://www.youtube.com/embed/link_for_lesson_3_2',
        'Lesson 3.3': 'https://www.youtube.com/embed/link_for_lesson_3_3',
        'Lesson 3.4': 'https://www.youtube.com/embed/link_for_lesson_3_4'
    }

    # Create a placeholder for the initial display
    video_url = tutorial_links['Lesson 3.1']  # Default video to display
    video_frame = components.html(
        f"<iframe width='560' height='315' src='{video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        height=315
    )

    # Two columns for buttons
    col1, col2 = st.columns(2)

    # Setup buttons to update the video iframe
    with col1:
        if st.button('Lesson 3.1'):
            video_frame = update_video(tutorial_links['Lesson 3.1'])
        if st.button('Lesson 3.2'):
            video_frame = update_video(tutorial_links['Lesson 3.2'])
    with col2:
        if st.button('Lesson 3.3'):
            video_frame = update_video(tutorial_links['Lesson 3.3'])
        if st.button('Lesson 3.4'):
            video_frame = update_video(tutorial_links['Lesson 3.4'])

def update_video(video_url):
    """Return an HTML component with a new video URL."""
    return components.html(
        f"<iframe width='560' height='315' src='{video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        height=315
    )

if __name__ == "__main__":
    main()
