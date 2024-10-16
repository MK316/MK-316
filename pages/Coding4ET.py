import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('Coding4ET Tutorials')

    # Tabs setup
    tabs = st.tabs(["Manual", "Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"])
    
    # Populate non-video tabs
    for i, tab in enumerate(tabs):
        if i != 3:
            with tab:
                st.write("To be updated.")

    # Special handling for Lesson 3
    with tabs[3]:
        st.subheader("Lesson 3 Videos")

        # Define video URLs
        video_links = {
            'Lesson 3.1': 'https://www.youtube.com/embed/uigxMFBR0Wg',
            'Lesson 3.2': 'https://www.youtube.com/embed/gPIe1Tgie1Q',
            'Lesson 3.3': 'https://www.youtube.com/embed/ofhRZ6k3Ryw',
            'Lesson 3.4': 'https://www.youtube.com/embed/vSsClackic4'
        }

        # Initialize session state for video URL
        if 'current_video' not in st.session_state:
            st.session_state.current_video = video_links['Lesson 3.1']

        # Video display
        components.html(
            get_iframe(st.session_state.current_video), height=300
        )

        # Setup buttons to update the video
        col = st.columns(1)[0]
        for lesson, url in video_links.items():
            if col.button(lesson):
                st.session_state.current_video = url
                components.html(
                    get_iframe(st.session_state.current_video), height=300
                )

def get_iframe(video_url):
    """Generate an iframe HTML element for the given video URL."""
    return f"""
    <iframe width='400' height='300' src='{video_url}' 
    frameborder='0' allow='accelerometer; autoplay; clipboard-write; 
    encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
    """

if __name__ == "__main__":
    main()
