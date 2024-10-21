import streamlit as st

def main():
    st.title("🐾 Language Tools X Future Educators")
    st.write("Welcome to our dynamic showcase of language applications, creatively designed by aspiring English teachers. These applications are crafted to enrich language learning and teaching experiences. Stay tuned—exciting developments are on the way! (To be updated)")

    # Path to the image
    image_path = 'data/octocat-2.png'

    # Display the image
    st.image(image_path, caption='Sample Image', use_column_width=True)

if __name__ == "__main__":
    main()
