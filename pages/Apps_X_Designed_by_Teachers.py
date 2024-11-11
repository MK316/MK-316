import streamlit as st

def main():
    st.title("🐾 Tools X Future Educators")
    st.write("Welcome to our dynamic showcase of language applications, creatively designed by aspiring English teachers. These applications are crafted to enrich language learning and teaching experiences. Stay tuned—exciting developments are on the way!")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("_(To be updated)_")
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Path to the image
    image_path = 'https://github.com/MK316/MK-316/raw/main/images/octocat-2-line.png'
            
    # Display the image
    st.image(image_path, width=600)

    # Display the caption with HTML for styling and line breaks
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        "The mediocre teacher tells. The good teacher explains.<br>
        The superior teacher demonstrates. The great teacher inspires." <br>
        - <span style='font-style: italic;'>W. A. Ward</span>
    </div>
    """, unsafe_allow_html=True)

    # Create multiple tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["Tab 1: 1. Verb tense practice", "Tab 2: 2. Noun plurals", "Tab 3: TBA", "Tab 4: TBA"])

    # Content for Tab 1
    with tab1:
        st.header("Practice verb froms Present - Past - Past Participle")
        st.write("Team #1: This project aims to implement an application that allows practice of the three forms of basic verbs that appear in high school textbooks. (November 2024)")

    # Content for Tab 2
    with tab2:
        st.header("Regular and irregular noun plural form practice")
        st.write("Team #2: This project aims to implement an application that allows practice of plural forms of English nouns.")

    # Content for Tab 3
    with tab3:
        st.header("Welcome to Tab 3")
        st.write("Here's a detailed look at the tools developed by future educators.")

    # Content for Tab 4
    with tab4:
        st.header("Welcome to Tab 4")
        st.write("Get inspired by the stories and successes of those who've used these tools.")

if __name__ == "__main__":
    main()
