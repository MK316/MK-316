import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('Coding4ET Tutorials')

    # Define video URLs (Use the "embed" link from YouTube)
    tutorial_links = {
        'Lesson 3.1': 'https://www.youtube.com/embed/link_for_lesson_3_1',
        'Lesson 3.2': 'https://www.youtube.com/embed/link_for_lesson_3_2',
        'Lesson 3.3': 'https://www.youtube.com/embed/link_for_lesson_3_3',
        'Lesson 3.4': 'https://www.youtube.com/embed/link_for_lesson_3_4'
    }

    # Placeholder for the video iframe
    video_container = st.empty()
    default_video_url = tutorial_links['Lesson 3.1']  # Default video to display
    components.html(
        f"<iframe width='560' height='315' src='{default_video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        height=315
    )

    # Two columns for buttons
    col1, col2 = st.columns(2)

    # Button setup in columns
    with col1:
        if st.button('Lesson 3.1'):
            components.html(
                f"<iframe width='560' height='315' src='{tutorial_links['Lesson 3.1']}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
                height=315, key='1'
            )
        if st.button('Lesson 3.2'):
            components.html(
                f"<iframe width='560' height='315' src='{tutorial_links['Lesson 3.2']}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
                height=315, key='2'
            )
    with col2:
        if st.button('Lesson 3.3'):
            components.html(
                f"<iframe width='560' height='315' src='{tutorial_links['Lesson 3.3']}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
                height=315, key='3'
            )
        if st.button('Lesson 3.4'):
            components.html(
                f"<iframe width='560' height='315' src='{tutorial_links['Lesson 3.4']}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
                height=315, key='4'
            )

if __name__ == "__main__":
    main()
