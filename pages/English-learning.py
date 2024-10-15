import streamlit as st  # Corrected the import alias to 'st', which is standard

# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
# Display the image
st.image(image_url, caption="\"Every student can learn, just not on the same day, or the same way.\" – George Evans", use_column_width=True)

def elearning_apps_page():
    st.title('📙 English Language Learning Apps')
    st.write('Applications for English learners.')

    # Describing your apps briefly
    st.markdown("""
    Explore our selection of English learning apps designed specifically for learners. These applications use interactive and innovative tools to improve vocabulary knowledge, pronunciation, listening skills, and phonetic awareness, providing effective resources and exercises.
    """)

    # First row with three columns
    col1, col2, col3 = st.columns(3)  # Define columns for the first row

    with col1:
        st.image("images/button01.png", width=100)
        if st.button('App 1: Word Frequency', key='1'):
            st.markdown("🌀[App link](https://mk-316-freqlist.hf.space/): Paste text and get wordlist based with frequency info", unsafe_allow_html=True)
            st.markdown("2024.01.23")
    with col2:
        st.image("images/button03.png", width=100)
        if st.button('App 2: Loanword pronunciation', key='2'):
            st.markdown("🌀[App link](https://mk-316-korean-english/): English loanwords (9,386); pronunciation comparison (kor-eng); ", unsafe_allow_html=True)
            st.markdown("2024.02.05")
    
    with col3:
        st.image("images/button03.png", width=100)
        if st.button('App 3: Sound and Spelling', key='3'):
            st.markdown("🌀[App link](https://mk-316-spelling.hf.space/): High frequency words; listen and try spelling", unsafe_allow_html=True)
            st.markdown("2024.01.18")
    
    # Add some space before the second row
    st.write("\n\n")

    # Second row with three columns
    col4, col5, col6 = st.columns(3)  # Correct typo here

    with col4:
        st.image("images/button01.png", width=100)
        if st.button('App 4: Summarization', key='4'):
            st.markdown("🌀[App link](https://mk-316-summarization.hf.space/): Text summarization using transformer", unsafe_allow_html=True)
            st.markdown("2024.10.14")

    with col5:
        st.image("images/button03.png", width=100)
        if st.button('App 5: Pronunciation Feedback', key='5'):
            st.markdown("🌀[App link](https://mk-316-pronunciationfeedback.hf.space/): Read/record texts and get feedback", unsafe_allow_html=True)
            st.markdown("2024.05.28")

    with col6:
        st.image("images/button03.png", width=100)
        if st.button('App 6: Oxford5K pronunciation', key='6'):
            st.markdown("🌀[App link](https://mk-316-oxford5k-audio.hf.space/): Oxford learners' vocabulary; pronunciation practice; listening", unsafe_allow_html=True)
            st.markdown("2024.02.03")

elearning_apps_page()
