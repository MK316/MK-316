import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('Coding4ET Tutorials')

    tabs = st.tabs(["Manual", "Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"])

    # Static content for other tabs
    for i, tab in enumerate(tabs):
        if i != 3:
            with tab:
                st.write("To be updated.")

    # Special handling for Lesson 3
    with tabs[3]:
        st.subheader("Lesson 3 Videos")

        # Define video URLs using correct YouTube embed links
        video_links = {
            'Lesson 3.1': 'https://www.youtube.com/embed/uigxMFBR0Wg',
            'Lesson 3.2': 'https://www.youtube.com/embed/gPIe1Tgie1Q',
            'Lesson 3.3': 'https://www.youtube.com/embed/ofhRZ6k3Ryw',
            'Lesson 3.4': 'https://www.youtube.com/embed/vSsClackic4'
        }

        # Create buttons and placeholders in a single column
        col = st.columns(1)[0]
        video_placeholders = {lesson: st.empty() for lesson in video_links}  # Dict to hold placeholders

        for lesson in video_links:
            if col.button(lesson):
                # When a button is clicked, update only the corresponding video placeholder
                video_placeholders[lesson].html(get_iframe(video_links[lesson]), height=300)

def get_iframe(video_url):
    """Generate HTML iframe code for embedding a YouTube video."""
    return f"<iframe width='400' height='300' src='{video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"

if __name__ == "__main__":
    main()
