import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('Coding4ET Tutorials')

    # Create tabs for each section of the tutorial
    tabs = st.tabs(["Manual", "Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"])
    
    # Populate each tab except for Lesson 3 with a placeholder text
    for index, tab in enumerate(tabs):
        if index != 3:  # Skip index 3 as it's for Lesson 3
            with tab:
                st.write("To be updated.")

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

        # Initialize or get the current video from the session state
        if 'current_video' not in st.session_state:
            st.session_state['current_video'] = video_links['Lesson 3.1']  # Default video

        # Display the video using the session state URL
        components.html(
            get_iframe(st.session_state['current_video']),
            height=300
        )

        # Create buttons for each lesson under Lesson 3 and update the session state on click
        for lesson, url in video_links.items():
            if st.button(lesson):
                st.session_state['current_video'] = url

def get_iframe(video_url):
    """Return HTML iframe code for embedding a YouTube video."""
    return f"<iframe width='400' height='300' src='{video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"

if __name__ == "__main__":
    main()
