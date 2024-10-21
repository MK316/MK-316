import streamlit as st

def main():
    st.title("🐾 Language Tools X Future Educators")
    st.write("Welcome to our dynamic showcase of language applications, creatively designed by aspiring English teachers. These applications are crafted to enrich language learning and teaching experiences. Stay tuned—exciting developments are on the way!")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("(To be updated)")
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

if __name__ == "__main__":
    main()
