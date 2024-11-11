import streamlit as st

def main():
    st.title("🐾 Tools X Future Educators")
    st.write("Welcome to our dynamic showcase of language applications, creatively designed by aspiring Pre-service English teachers. These applications are crafted to enrich language learning and teaching experiences. Stay tuned—exciting developments are on the way!")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("_(To be updated)_")
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Path to the image
    image_path = 'https://github.com/MK316/MK-316/raw/main/images/octocat-2-line.png'
            
    # Display the image
    st.image(image_path, width=600)


if __name__ == "__main__":
    main()
