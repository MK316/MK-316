import streamlit as st

def main():
    st.title('Coding4ET Tutorials')

    # Layout: two columns for buttons
    col1, col2 = st.columns(2)

    # Defining button labels and corresponding URLs
    tutorial_links = {
        'Lesson 3.1': 'https://youtu.be/uigxMFBR0Wg',
        'Lesson 3.2': 'https://youtu.be/gPIe1Tgie1Q',
        'Lesson 3.3': 'https://youtu.be/ofhRZ6k3Ryw',
        'Lesson 3.4': 'https://youtu.be/vSsClackic4'
    }

    # Placing buttons in columns
    tutorials_in_col1 = ['Lesson 3.1', 'Lesson 3.2']
    tutorials_in_col2 = ['Lesson 3.3', 'Lesson 3.4']

    with col1:
        for lesson in tutorials_in_col1:
            if st.button(lesson):
                video_url = tutorial_links[lesson]
                st.video(video_url)

    with col2:
        for lesson in tutorials_in_col2:
            if st.button(lesson):
                video_url = tutorial_links[lesson]
                st.video(video_url)

if __name__ == "__main__":
    main()
