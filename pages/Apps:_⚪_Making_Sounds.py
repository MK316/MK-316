import streamlit as st
from pydub import AudioSegment
import io
from gtts import gTTS  # Google Text-to-Speech
import tempfile

# Convert MP3 to WAV function
def convert_to_wav(audio_file):
    try:
        sound = AudioSegment.from_mp3(audio_file)
        buffer = io.BytesIO()
        sound.export(buffer, format="wav")
        buffer.seek(0)
        return buffer
    except Exception as e:
        st.error(f"An error occurred: {str(e)}. This format may require external dependencies not available in this environment.")

def text_to_speech(text, language):
    lang_code = {
        "🇰🇷 Korean": {"lang": "ko", "tld": None},
        "🇺🇸 English (AmE)": {"lang": "en", "tld": "us"},
        "🇬🇧 English (BrE)": {"lang": "en", "tld": "co.uk"},  # Use tld for UK English
        "🇫🇷 French": {"lang": "fr", "tld": None},
        "🇪🇸 Spanish": {"lang": "es", "tld": None},
        "🇨🇳 Chinese": {"lang": "zh", "tld": None},
        "🇯🇵 Japanese": {"lang": "ja", "tld": None}
    }

    try:
        lang = lang_code[language]["lang"]
        tld = lang_code[language]["tld"]

        if tld:
            tts = gTTS(text=text, lang=lang, tld=tld)
        else:
            tts = gTTS(text=text, lang=lang)

        temp_file = tempfile.NamedTemporaryFile(delete=False)
        tts.save(temp_file.name)
        return temp_file.name
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None


# Phonetics Apps Page
def phonetics_apps_page():
    st.title('🐾 Play sound Apps')
    st.write('Applications used to teach Phonetics.')
    st.markdown("""
    Here is a selection of audio-related applications specifically designed to enhance phonetics learning. These tools cater to various needs, such as playing audio files, converting file formats, and utilizing Text-to-Speech technology. They offer interactive exercises to improve pronunciation, develop listening skills, and heighten phonetic awareness, making them invaluable resources for learners and educators alike.
    """)

    tab1, tab2, tab3 = st.tabs(["🔎Audio Speed Adjuster", "🔎MP3-to-WAV", "🔎Multi-TTS"])

    # Tab 1: Audio Speed Adjuster
    with tab1:
        st.header("Audio Speed Adjuster")
        st.write("Please upload WAV files only for speed adjustment.")
        st.markdown("If you have MP3 or other audio formats, please first convert them to WAV using this tool: [MP3 to WAV Converter](https://huggingface.co/spaces/MK-316/mp3towav)")
        uploaded_file = st.file_uploader("Upload an audio file", type=['wav'])

        if uploaded_file is not None:
            try:
                sound = AudioSegment.from_file(uploaded_file, format='wav')
                speed = st.slider("Adjust Speed", 0.5, 2.0, 1.0, step=0.1)
                modified_sound = sound.speedup(playback_speed=speed)

                buffer = io.BytesIO()
                modified_sound.export(buffer, format="wav")
                buffer.seek(0)
                st.audio(buffer, format='audio/wav')
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.error("Please ensure the file is a WAV format.")

    # Tab 2: MP3 to WAV Converter
    with tab2:
        st.header("MP3 to WAV Converter")
        audio_file = st.file_uploader("Upload MP3 file", type=['mp3'])

        if audio_file is not None:
            wav_buffer = convert_to_wav(audio_file)
            if wav_buffer is not None:
                st.audio(wav_buffer, format='audio/wav')

    # Tab 3: Multi-Text to Speech Application
    with tab3:
        st.header("Multi-Text to Speech Application")
        st.write("Enter text and choose a language to generate the corresponding audio.")
        user_input = st.text_area("Enter text here...")
        language = st.selectbox("Language", ["🇰🇷 Korean", "🇺🇸 English (AmE)", "🇬🇧 English (BrE)", "🇫🇷 French", "🇪🇸 Spanish", "🇨🇳 Chinese", "🇯🇵 Japanese"])
        submit_button = st.button('Generate Speech')

        if submit_button:
            if user_input:
                audio_file_path = text_to_speech(user_input, language)
                if audio_file_path:
                    with open(audio_file_path, "rb") as audio_file:
                        st.audio(audio_file, format='audio/mp3')

# Run the phonetics apps page
phonetics_apps_page()
