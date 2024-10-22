import streamlit as st
from gtts import gTTS
import io

# Function to handle text-to-speech conversion
def text_to_speech(text, language, tld):
    try:
        tts = gTTS(text=text, lang=language, tld=tld)
        buffer = io.BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)
        return buffer
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Function to convert language and dialect choices
def get_language_tld(language_choice):
    if language_choice == "🇰🇷 Korean":
        return 'ko', 'ko'
    elif language_choice == "🇬🇧 English (United Kingdom)":
        return 'en', 'co.uk'
    elif language_choice == "🇺🇸 English (United States)":
        return 'en', 'us'
    elif language_choice == "🇨🇦 English (Canada)":
        return 'en', 'ca'
    elif language_choice == "🇦🇺 English (Australia)":
        return 'en', 'com.au'
    elif language_choice == "🇮🇳 English (India)":
        return 'en', 'co.in'
    elif language_choice == "🇿🇦 English (South Africa)":
        return 'en', 'co.za'
    elif language_choice == "🇳🇬 English (Nigeria)":
        return 'en', 'com.ng'
    elif language_choice == "🇫🇷 French (France)":
        return 'fr', 'fr'
    elif language_choice == "🇨🇳 Mandarin (China Mainland)":
        return 'zh-CN', 'any'
    else:
        return 'en', 'us'  # Default to US English

# Main Streamlit app
st.title("Multi-Text to Speech Application")
st.write("Enter text and choose a language to generate the corresponding audio.")

# User input for text
user_input = st.text_area("Enter text here...")

# Language selection with dialect options
language_choice = st.selectbox(
    "Choose a language and dialect",
    ["🇰🇷 Korean", "🇬🇧 English (United Kingdom)", "🇺🇸 English (United States)", 
     "🇨🇦 English (Canada)", "🇦🇺 English (Australia)", "🇮🇳 English (India)", 
     "🇿🇦 English (South Africa)", "🇳🇬 English (Nigeria)", "🇫🇷 French (France)", 
     "🇨🇳 Mandarin (China Mainland)""]
)

# Submit button
submit_button = st.button('Generate Speech')

if submit_button:
    if user_input:
        # Get language code and tld based on the choice
        lang, tld = get_language_tld(language_choice)
        
        # Generate speech
        audio_file = text_to_speech(user_input, lang, tld)
        
        # Play the audio file
        st.audio(audio_file, format='audio/mp3', start_time=0)
