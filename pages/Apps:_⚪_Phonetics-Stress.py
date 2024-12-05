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

# Functions for Tab 2 (Syllable Structure Visualizer)
def parse_syllables(syllable_input):
    syllables = syllable_input.split(".")  # Split syllables by .
    parsed_syllables = []
    for syllable in syllables:
        is_stressed = syllable.startswith("ˈ")  # Check for stress marker
        if is_stressed:
            syllable = syllable[1:]  # Remove stress marker for processing
        if "//" in syllable:  # Handle syllabic consonants
            parts = syllable.split("//")
            if len(parts) == 3:  # Onset, Syllabic Consonant (Nucleus + Coda)
                onset, nucleus_coda = parts[0], parts[1]
                parsed_syllables.append({"Onset": onset, "Nucleus_Coda": nucleus_coda, "Syllabic": True, "Stress": is_stressed})
            elif len(parts) == 2:  # No onset, only Syllabic Consonant
                nucleus_coda = parts[1]
                parsed_syllables.append({"Onset": "", "Nucleus_Coda": nucleus_coda, "Syllabic": True, "Stress": is_stressed})
        elif "/" in syllable:  # Handle regular vowels
            parts = syllable.split("/")
            if len(parts) == 3:  # Onset, Nucleus, Coda
                onset, nucleus, coda = parts[0], parts[1], parts[2]
                parsed_syllables.append({"Onset": onset, "Nucleus": nucleus, "Coda": coda, "Syllabic": False, "Stress": is_stressed})
            elif len(parts) == 2:  # Only Onset and Nucleus or Nucleus and Coda
                onset, nucleus, coda = parts[0], parts[1], ""
                parsed_syllables.append({"Onset": onset, "Nucleus": nucleus, "Coda": coda, "Syllabic": False, "Stress": is_stressed})
            else:  # Only Nucleus
                onset, nucleus, coda = "", parts[1], ""
                parsed_syllables.append({"Onset": onset, "Nucleus": nucleus, "Coda": coda, "Syllabic": False, "Stress": is_stressed})
        else:
            parsed_syllables.append({"Onset": "", "Nucleus": "", "Coda": "", "Syllabic": False, "Stress": is_stressed})
    return parsed_syllables

def format_with_slashes(text):
    """Format text with double slashes."""
    if text.startswith("/") and text.endswith("/"):
        return text  # If already has slashes, return as is
    return f"/{text}/"  # Otherwise, add slashes

def create_syllable_tree(syllable_data, syllable_number):
    """Create a syllable tree showing Onset, Rhyme, Nucleus, and Coda."""
    graph = graphviz.Digraph(format="png")
    syllable_color = "orange" if syllable_data.get("Stress") else "white"

    # Main Syllable node
    graph.node(f"Syllable{syllable_number}", "Syllable", shape="ellipse", style="filled", fillcolor=syllable_color)

    # Onset node
    if syllable_data.get("Onset"):
        graph.node(f"Onset{syllable_number}", f"Onset\n{format_with_slashes(syllable_data['Onset'])}", shape="ellipse")
        graph.edge(f"Syllable{syllable_number}", f"Onset{syllable_number}")

    # Rhyme node
    graph.node(f"Rhyme{syllable_number}", "Rhyme", shape="ellipse")
    graph.edge(f"Syllable{syllable_number}", f"Rhyme{syllable_number}")

    if syllable_data.get("Syllabic"):  # Syllabic consonant
        graph.node(
            f"Nucleus_Coda{syllable_number}",
            f"Nucleus/Coda\n{format_with_slashes(syllable_data['Nucleus_Coda'])}",
            shape="ellipse",
        )
        graph.edge(f"Rhyme{syllable_number}", f"Nucleus_Coda{syllable_number}")
    else:
        # Nucleus node
        if syllable_data.get("Nucleus"):
            graph.node(f"Nucleus{syllable_number}", f"Nucleus\n{format_with_slashes(syllable_data['Nucleus'])}", shape="ellipse")
            graph.edge(f"Rhyme{syllable_number}", f"Nucleus{syllable_number}")

        # Coda node (if not empty)
        if syllable_data.get("Coda") and syllable_data.get("Coda").strip():
            graph.node(f"Coda{syllable_number}", f"Coda\n{format_with_slashes(syllable_data['Coda'])}", shape="ellipse")
            graph.edge(f"Rhyme{syllable_number}", f"Coda{syllable_number}")

    return graph


# Multi-tab layout
tabs = st.tabs(["Word Stress", "Syllable Structure"])

with tabs[0]:
    st.title("📚 Word Search")
    st.caption("This app displays the stress, part of speech, and transcription for words from Chapter 7 of the textbook. Enter the word you want to look up in the text box below and click **Submit**.")

    # Input box for user to enter a word
    user_input = st.text_input("Enter a word to search:", placeholder="Type a word here...")

    # Button for mobile users to trigger result
    if st.button("Submit"):
        if user_input:
            # Search the word in the dataset
            result = df[df['Word'].str.lower() == user_input.lower()]
            if result.empty:
                st.error("The word is not in the list.")
            else:
                # Extract word details
                pos = result.iloc[0]['POS']
                full_pos = convert_pos(pos)
                stress = result.iloc[0]['Stress']
                transcription = result.iloc[0]['Transcription']
                word = result.iloc[0]['Word']

                # Generate TTS audio
                tts = gTTS(word)
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
                tts.save(temp_file.name)

                # Display the result
                st.markdown(f"""
                <div style='font-size: 16px; padding: 10px; border: 6px solid #9FD497; border-radius: 10px;'>
                    <strong>⚪ POS:</strong> {full_pos}<br>
                    <strong>⚪ Stress:</strong> {stress}<br>
                    <strong>⚪ Transcription:</strong> {transcription}
                </div>
                """, unsafe_allow_html=True)
            st.write("")
            st.caption("The audio below uses Google TTS with American accent.") 
            st.audio(temp_file.name)
        else:
            st.error("Please enter a word to search.")

# Tab 2: Syllable Structure Visualizer
with tabs[1]:
    st.title("🌳 Syllable Structure Visualizer")
    st.markdown("""
    ### 🔳 Instructions:
    1. Enter a word using IPA symbols ([Visit IPA online website](https://ipa.typeit.org/))

    2. Use:
       - `.` for syllable boundaries.
       - `/` to mark **both sides** of the nucleus.
       - `//` to mark **syllabic consonants** (e.g., `//n//`).
       - `ˈ` before a syllable to mark **stress**.
    3. Example: ˈstr/ɛ/ŋ.θ//n// for [strɛŋθn̩]
    """)

    syllable_input = st.text_input("Enter syllabified text:", placeholder="e.g., ˈstr/ɛ/.ŋ/θ/.//n//")
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
            st.error("Please enter syllabified text.")
