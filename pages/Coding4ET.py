import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('Coding4ET Tutorials')

    tabs = st.tabs(["Manual", "Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5"])
    
    for tab, content in zip(tabs, ["To be updated"] * 5):
        with tab:
            st.write(content)

    # Handling the Lesson 3 with video links
    with tabs[3]:
        st.subheader("Lesson 3 Videos")
        # Define video URLs
        video_links = {
            'Lesson 3.1': 'https://youtu.be/uigxMFBR0Wg',
            'Lesson 3.2': 'https://youtu.be/gPIe1Tgie1Q',
            'Lesson 3.3': 'https://youtu.be/ofhRZ6k3Ryw',
            'Lesson 3.4': 'https://youtu.be/vSsClackic4'
        }

        # Initialize a video placeholder
        video_placeholder = st.empty()
        video_url = video_links['Lesson 3.1']  # Default video
        video_placeholder.html(get_iframe(video_url), height=300)

        # Display buttons and update video on click
        for lesson in video_links:
            if st.button(lesson):
                video_url = video_links[lesson]
                video_placeholder.html(get_iframe(video_url), height=300)

def get_iframe(video_url):
    return f"<iframe width='400' height='300' src='{video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"

if __name__ == "__main__":
    main()
