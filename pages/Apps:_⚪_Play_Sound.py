import streamlit as st
from pydub import AudioSegment
import io

def speed_change(sound, speed=1.0):
    # Change the playback speed of the audio without changing the pitch
    new_frame_rate = int(sound.frame_rate * speed)
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_frame_rate})

def phonetics_apps_page():
    st.title('🐾 Play sound Apps')
    st.write('Applications used to teach Phonetics.')
    st.markdown("""
    Here is a selection of audio-related applications specifically designed to enhance phonetics learning. These tools cater to various needs, such as playing audio files, converting file formats, and utilizing Text-to-Speech technology. They offer interactive exercises to improve pronunciation, develop listening skills, and heighten phonetic awareness, making them invaluable resources for learners and educators alike.
    """)

    tab1, tab2, tab3 = st.tabs(["Audio Speed Adjuster", "MP3-to-wav", "Multi-TTS"])

    with tab1:
        st.header("Audio Speed Adjuster")
        st.write("Please upload WAV files only for speed adjustment.")
        st.markdown("If you have MP3 or other audio formats, please first convert them to WAV using this tool: [MP3 to WAV Converter](https://huggingface.co/spaces/MK-316/mp3towav)")
        uploaded_file = st.file_uploader("Upload an audio file", type=['wav'])

        if uploaded_file is not None:
            try:
                sound = AudioSegment.from_file(uploaded_file, format='wav')
                speed = st.slider("Adjust Speed", 0.5, 2.0, 1.0, step=0.1)
                modified_sound = speed_change(sound, speed=speed)

                buffer = io.BytesIO()
                modified_sound.export(buffer, format="wav")
                buffer.seek(0)
                st.audio(buffer, format='audio/wav')
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.error("Please ensure the file is a WAV format.")

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
