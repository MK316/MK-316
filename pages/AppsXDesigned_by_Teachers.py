import streamlit as st

def main():
    st.title("💭 Language Tools X English Teachers")
    st.write("Welcome to our curated showcase of language applications, thoughtfully created by active English teachers. These tools are developed with real classroom experiences in mind to enhance both learning and teaching of languages. Stay tuned—exciting new tools are on the way!")
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

if __name__ == "__main__":
    main()
