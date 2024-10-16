import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('Coding4ET Tutorials')

    # Create tabs for each section of the tutorial
    tabs = st.tabs(["Manual", "Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"])
    
    # Populate each tab except for Lesson 3 with a placeholder text
    for tab, content in zip(tabs, ["To be updated"] * 5):
        with tab:
            st.write(content)

    # Handling the Lesson 3 with video links
    with tabs[3]:
        st.subheader("Lesson 3 Videos")
        
        # Define video URLs using the correct YouTube embed links
        video_links = {
            'Lesson 3.1': 'https://www.youtube.com/embed/uigxMFBR0Wg',
            'Lesson 3.2': 'https://www.youtube.com/embed/gPIe1Tgie1Q',
            'Lesson 3.3': 'https://www.youtube.com/embed/ofhRZ6k3Ryw',
            'Lesson 3.4': 'https://www.youtube.com/embed/vSsClackic4'
        }

        # Initialize a video placeholder
        video_placeholder = st.empty()
        video_url = video_links['Lesson 3.1']  # Display the default video initially
        video_placeholder.html(get_iframe(video_url), height=300)

        # Create buttons for each lesson under Lesson 3 and update the video on click
        for lesson in video_links:
            if st.button(lesson):
                video_url = video_links[lesson]
                video_placeholder.html(get_iframe(video_url), height=300)

def get_iframe(video_url):
    """Return HTML iframe code for embedding a YouTube video."""
    return f"<iframe width='400' height='300' src='{video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"

if __name__ == "__main__":
    main()
