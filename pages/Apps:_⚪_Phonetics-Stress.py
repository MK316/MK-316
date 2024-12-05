import streamlit as st
import pandas as pd
from gtts import gTTS
import tempfile

# Load the dataset from GitHub
csv_url = "https://raw.githubusercontent.com/MK316/stress2024/refs/heads/main/data/stressdata1.csv"
df = pd.read_csv(csv_url)

# POS mapping for full form
pos_mapping = {
    "n": "Noun",
    "adj": "Adjective",
    "v": "Verb",
    "adv": "Adverb"
}

def convert_pos(pos_abbreviations):
    """Convert POS abbreviations to full forms."""
    pos_list = [pos_mapping[abbreviation.strip()] for abbreviation in pos_abbreviations.split(",") if abbreviation.strip() in pos_mapping]
    return ", ".join(pos_list)

# Set up the tabs
tabs = st.tabs(["Word Stress", "Tab 2", "Tab 3", "Tab 4"])

# First Tab: Word Stress
with tabs[0]:
    st.title("📚 Word Stress (Searching Engine)")
    st.caption("This app displays the stress, part of speech, and transcription for words from Chapter 7 of the textbook. Enter the word you want to look up in the text box below.")

    # User input for searching a word
    user_input = st.text_input("Enter a word to search:", placeholder="Type a word here...")

    # Search functionality
    if user_input:
        # Check if the word exists in the 'Word' column
        result = df[df['Word'].str.lower() == user_input.lower()]
        if result.empty:
            st.error("The word is not in the list.")
        else:
            # Extract details for the word
            pos = result.iloc[0]['POS']
            full_pos = convert_pos(pos)
            stress = result.iloc[0]['Stress']
            transcription = result.iloc[0]['Transcription']
            word = result.iloc[0]['Word']

            # Generate audio using gTTS
            tts = gTTS(word)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_file.name)

            # Display the results in a flashcard style
            st.markdown(f"<div style='font-size: 24px; padding: 10px; border: 6px solid #9FD497; border-radius: 10px;'>"
                        f"<strong>⚪ POS:</strong> {full_pos}<br>"
                        f"<strong>⚪ Stress:</strong> {stress}<br>"
                        f"<strong>⚪ Transcription:</strong> {transcription}"
                        f"</div>", unsafe_allow_html=True)

            # Add the audio player
            st.write("")
            st.caption("The audio below uses Google TTS and plays the word with an American accent.")
            st.audio(temp_file.name)

# Second Tab: Placeholder
with tabs[1]:
    st.title("Tab 2")
    st.write("This is Tab 2. You can add any content you want here.")

# Third Tab: Placeholder
with tabs[2]:
    st.title("Tab 3")
    st.write("This is Tab 3. Add your content for this section.")

# Fourth Tab: Placeholder
with tabs[3]:
    st.title("Tab 4")
    st.write("This is Tab 4. Customize this page as needed.")
