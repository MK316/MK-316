import streamlit as st
import pandas as pd
import tempfile
from gtts import gTTS

# Load the dataset from GitHub
@st.cache
def load_data(url):
    return pd.read_csv(url)

csv_url = "https://raw.githubusercontent.com/MK316/stress2024/refs/heads/main/data/stressdata1.csv"
df = load_data(csv_url)

# POS mapping
pos_mapping = {
    "n": "Noun",
    "adj": "Adjective",
    "v": "Verb",
    "adv": "Adverb"
}

# Convert POS abbreviations to full forms
def convert_pos(pos_abbrev):
    return ", ".join([pos_mapping.get(p.strip(), p.strip()) for p in pos_abbrev.split(',')])

# Main app layout
st.title("Words-by-stress")
stress_options = ["1st", "2nd", "antepenult", "penult", "ult"]
selected_stress = None

# Display button for each stress option with color change on select
cols = st.columns(len(stress_options))
for idx, option in enumerate(stress_options):
    if cols[idx].button(option, key=option, help=f"Show words with {option} stress"):
        selected_stress = option

# Display data based on selected stress
if selected_stress:
    filtered_data = df[df['Stress'] == selected_stress]
    st.write(f"Total words with '{selected_stress}' stress: {len(filtered_data)}")
    st.dataframe(filtered_data[['Word', 'POS', 'Transcription']])
    for idx, option in enumerate(stress_options):
        if option == selected_stress:
            cols[idx].markdown(f"<h1 style='color: yellow;'>{option}</h1>", unsafe_allow_html=True)
        else:
            cols[idx].markdown(f"<h1 style='color: gray;'>{option}</h1>", unsafe_allow_html=True)

# Word Search with Audio Playback
st.title("Word Search")
user_input = st.text_input("Enter a word to search:", placeholder="Type a word here...")

if st.button("Search"):
    result = df[df['Word'].str.lower() == user_input.lower()]
    if result.empty:
        st.error("The word is not in the list.")
    else:
        pos = result.iloc[0]['POS']
        full_pos = convert_pos(pos)
        stress = result.iloc[0]['Stress']
        transcription = result.iloc[0]['Transcription']
        word = result.iloc[0]['Word']

        tts = gTTS(text=word, lang='en')
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        st.write(f"POS: {full_pos}")
        st.write(f"Stress: {stress}")
        st.write(f"IPA: {transcription}")
        st.audio(temp_file.name)
