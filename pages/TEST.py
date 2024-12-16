import streamlit as st
import pandas as pd
import graphviz
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

# Function to add visual circles for stress patterns
def add_stress_circles(stress):
    graph = graphviz.Digraph(format="png")
    graph.attr(rankdir="LR")  # Arrange nodes left-to-right
    for option in ["ult", "penult", "antepenult", "1st", "2nd"]:
        color = "yellow" if option == stress else "lightgrey"
        graph.node(option, option.capitalize(), style='filled', fillcolor=color)
    return graph

# Main app layout
st.title("Words-by-stress")
stress_options = ["1st", "2nd", "...", "antepenult", "penult", "ult"]
selected_stress = st.selectbox("Select Stress", stress_options)

# Display data based on selected stress
if selected_stress and selected_stress != "...":
    filtered_data = df[df['Stress'] == selected_stress]
    st.write(f"Total words with '{selected_stress}' stress: {len(filtered_data)}")
    st.dataframe(filtered_data[['Word', 'POS', 'Transcription']])
    st.graphviz_chart(add_stress_circles(selected_stress))

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
