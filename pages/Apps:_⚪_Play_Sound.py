import streamlit as st
from gtts import gTTS
from io import BytesIO

def text_to_speech(text, language):
    language_map = {
        "🇰🇷 Korean": "ko",
        "🇺🇸 English (AmE)": ("en", "us"),
        "🇬🇧 English (BrE)": ("en", "co.uk"),
        "🇫🇷 French": "fr",
        "🇪🇸 Spanish": ("es", "es"),
        "🇨🇳 Chinese": "zh-CN"
    }

    if isinstance(language_map[language], tuple):
        lang, tld = language_map[language]
        tts = gTTS(text=text, lang=lang, tld=tld)
    else:
        lang = language_map[language]
        tts = gTTS(text=text, lang=lang)

    # Save to bytes buffer instead of a file
    mp3_fp = BytesIO()
    tts.save(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp

def phonetics_apps_page():
    st.title('🐾 Play sound Apps')
    st.write('Applications used to teach Phonetics.')
    st.markdown("""
    Here is a selection of audio-related applications specifically designed to enhance phonetics learning. These tools cater to various needs, such as playing audio files, converting file formats, and utilizing Text-to-Speech technology. They offer interactive exercises to improve pronunciation, develop listening skills, and heighten phonetic awareness, making them invaluable resources for learners and educators alike.
    """)
    tab1, tab2, tab3 = st.tabs(["Play audio", "MP3-to-wav", "Multi-TTS"])

    with tab1:
        st.image("images/button03.png", width=100)
        st.markdown("🌀 [App link](https://playsound.streamlit.app/): Upload audio to play; Speed controller", unsafe_allow_html=True)

    with tab2:
        st.image("images/button03.png", width=100)
        st.markdown("🌀 [App link](https://mk-316-mp3towav.hf.space/): Convert mp3 to wav file", unsafe_allow_html=True)

    with tab3:
        st.header("Multi-Text to Speech Application")
        st.write("Enter text and choose a language to generate the corresponding audio.")
        user_input = st.text_area("Enter text here...")
        language = st.selectbox("Language", ["🇰🇷 Korean", "🇺🇸 English (AmE)", "🇬🇧 English (BrE)", "🇫🇷 French", "🇪🇸 Spanish", "🇨🇳 Chinese"])
        submit_button = st.button('Generate Speech')

        if submit_button:
            if user_input:
                audio_file = text_to_speech(user_input, language)
                st.audio(audio_file, format='audio/mp3', start_time=0)

phonetics_apps_page()
