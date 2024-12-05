import streamlit as st
import pandas as pd
from gtts import gTTS
import tempfile
import graphviz

# Load the dataset from GitHub for Tab 1
csv_url = "https://raw.githubusercontent.com/MK316/stress2024/refs/heads/main/data/stressdata1.csv"
df = pd.read_csv(csv_url)

# POS mapping for Tab 1
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

def format_with_slashes(text):
    """Format text with slashes."""
    if text.startswith("/") and text.endswith("/"):
        return text
    return f"/{text}/"

def parse_single_syllable(input_syllable):
    """Parse a single stressed syllable into its components."""
    is_stressed = input_syllable.startswith("ˈ")
    if is_stressed:
        input_syllable = input_syllable[1:]  # Remove stress marker

    if "/" in input_syllable:  # Handle regular vowels
        parts = input_syllable.split("/")
        if len(parts) == 3:  # Onset, Nucleus, Coda
            return {"Onset": parts[0], "Nucleus": parts[1], "Coda": parts[2], "Stress": is_stressed}
        elif len(parts) == 2:  # Onset and Nucleus only
            return {"Onset": parts[0], "Nucleus": parts[1], "Coda": "", "Stress": is_stressed}
        elif len(parts) == 1:  # Nucleus only
            return {"Onset": "", "Nucleus": parts[0], "Coda": "", "Stress": is_stressed}
    return {"Onset": "", "Nucleus": "", "Coda": "", "Stress": is_stressed}

# Function to parse syllable input
def parse_syllables(syllable_input):
    """Parse syllable input into components, including double-slash syllables."""
    syllables = syllable_input.split(".")  # Split syllables by .
    parsed_syllables = []
    for syllable in syllables:
        is_stressed = syllable.startswith("ˈ")  # Check for stress marker
        if is_stressed:
            syllable = syllable[1:]  # Remove stress marker for processing
        if "//" in syllable:  # Handle syllabic consonants
            parts = syllable.split("//")
            if len(parts) == 2:  # Onset and Syllabic consonant
                parsed_syllables.append({
                    "Onset": parts[0],
                    "Nucleus": "",
                    "Coda": parts[1],
                    "Stress": is_stressed,
                    "Syllabic": True
                })
            elif len(parts) == 1:  # Only Syllabic consonant
                parsed_syllables.append({
                    "Onset": "",
                    "Nucleus": "",
                    "Coda": parts[0],
                    "Stress": is_stressed,
                    "Syllabic": True
                })
        elif "/" in syllable:  # Handle regular vowels
            parts = syllable.split("/")
            if len(parts) == 3:  # Onset, Nucleus, Coda
                parsed_syllables.append({
                    "Onset": parts[0],
                    "Nucleus": parts[1],
                    "Coda": parts[2],
                    "Stress": is_stressed,
                    "Syllabic": False
                })
            elif len(parts) == 2:  # Onset and Nucleus only
                parsed_syllables.append({
                    "Onset": parts[0],
                    "Nucleus": parts[1],
                    "Coda": "",
                    "Stress": is_stressed,
                    "Syllabic": False
                })
            elif len(parts) == 1:  # Nucleus only
                parsed_syllables.append({
                    "Onset": "",
                    "Nucleus": parts[0],
                    "Coda": "",
                    "Stress": is_stressed,
                    "Syllabic": False
                })
    return parsed_syllables

def create_syllable_tree(syllable_data, syllable_number):
    """Create a syllable tree showing Onset, Rhyme, Nucleus, and Coda."""
    graph = graphviz.Digraph(format="png")
    syllable_color = "yellow" if syllable_data.get("Stress") else "white"

    # Main Syllable node
    graph.node(f"Syllable{syllable_number}", "Syllable", shape="ellipse", style="filled", fillcolor=syllable_color)

    # Onset node
    if syllable_data.get("Onset"):
        graph.node(f"Onset{syllable_number}", f"Onset\n{format_with_slashes(syllable_data['Onset'])}", shape="ellipse")
        graph.edge(f"Syllable{syllable_number}", f"Onset{syllable_number}")

    # Rhyme node
    graph.node(f"Rhyme{syllable_number}", "Rhyme", shape="ellipse")
    graph.edge(f"Syllable{syllable_number}", f"Rhyme{syllable_number}")

    # Nucleus node
    if syllable_data.get("Nucleus"):
        graph.node(f"Nucleus{syllable_number}", f"Nucleus\n{format_with_slashes(syllable_data['Nucleus'])}", shape="ellipse")
        graph.edge(f"Rhyme{syllable_number}", f"Nucleus{syllable_number}")

    # Coda node (if not empty)
    if syllable_data.get("Coda").strip():
        graph.node(f"Coda{syllable_number}", f"Coda\n{format_with_slashes(syllable_data['Coda'])}", shape="ellipse")
        graph.edge(f"Rhyme{syllable_number}", f"Coda{syllable_number}")

    return graph

# Multi-tab layout
tabs = st.tabs(["Word Stress", "Stressed syllable", "Syllable Structure", "Tab 4"])

# Tab 1: Word Stress
with tabs[0]:
    st.title("📚 Word Stress (Searching Engine)")
    st.caption("This app displays the stress, part of speech, and transcription for words from Chapter 7 of the textbook. Enter the word you want to look up in the text box below.")

    user_input = st.text_input("Enter a word to search:", placeholder="Type a word here...")
    if user_input:
        result = df[df['Word'].str.lower() == user_input.lower()]
        if result.empty:
            st.error("The word is not in the list.")
        else:
            pos = result.iloc[0]['POS']
            full_pos = convert_pos(pos)
            stress = result.iloc[0]['Stress']
            transcription = result.iloc[0]['Transcription']
            word = result.iloc[0]['Word']

            tts = gTTS(word)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_file.name)

            st.markdown(f"<div style='font-size: 24px; padding: 10px; border: 6px solid #9FD497; border-radius: 10px;'>"
                        f"<strong>⚪ POS:</strong> {full_pos}<br>"
                        f"<strong>⚪ Stress:</strong> {stress}<br>"
                        f"<strong>⚪ Transcription:</strong> {transcription}"
                        f"</div>", unsafe_allow_html=True)
            st.audio(temp_file.name)

# Tab 2: Stressed Syllable
with tabs[1]:
    st.title("🌟 Stressed Syllable Visualizer")
    st.markdown("### Instructions: Enter a single stressed syllable, e.g., `ˈstr/ɛ/`.")
    syllable_input = st.text_input("Enter a single stressed syllable:", placeholder="e.g., ˈstr/ɛ/")
    if st.button("Visualize Stressed Syllable"):
        if syllable_input:
            syllable_data = parse_single_syllable(syllable_input)
            if syllable_data.get("Stress"):
                tree = create_syllable_tree(syllable_data, 1)
                st.graphviz_chart(tree)
            else:
                st.error("Invalid stressed syllable. Please try again.")
        else:
            st.error("Please enter a syllable to visualize.")

# Tab 3: Syllable Structure Visualizer
with tabs[2]:
    st.title("🌳 Syllable Structure Visualizer")
    st.markdown("""
    ### 🔳 Instructions:
    1. Enter a word using IPA symbols ([Visit IPA online website](https://ipa.typeit.org/))

    2. Use:
       - . for syllable boundaries.
       - / to mark **both sides** of the nucleus.
       - // to mark **syllabic consonants** (e.g., //n//).
       - ˈ before a syllable to mark **stress**.
    3. Example: ˈstr/ɛ/ŋ.θ//n// for [strɛŋθn̩]
    """)

    # Input box for syllabified text
    syllable_input = st.text_input("Enter syllabified text:", placeholder="e.g., ˈstr/ɛ/.ŋ/θ/.//n//")

    # Button to generate the syllable trees
    if st.button("Generate Tree"):
        if syllable_input:
            syllables = parse_syllables(syllable_input)
            if syllables:
                for i, syllable_data in enumerate(syllables, start=1):
                    st.markdown(f"### Syllable {i}")
                    tree = create_syllable_tree(syllable_data, i)
                    st.graphviz_chart(tree)
            else:
                st.error("No valid syllables found. Please check your input.")
        else:
            st.error("Please enter valid syllabified text.")
