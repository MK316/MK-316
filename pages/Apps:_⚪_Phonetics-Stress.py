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

# Functions for Syllable Structure in Tab 2
def parse_syllables(syllable_input):
    """Parse syllable input into components."""
    syllables = syllable_input.split(".")
    parsed_syllables = []
    for syllable in syllables:
        is_stressed = syllable.startswith("ˈ")
        if is_stressed:
            syllable = syllable[1:]
        if "//" in syllable:
            parts = syllable.split("//")
            if len(parts) == 3:
                onset, nucleus_coda = parts[0], parts[1]
                parsed_syllables.append({"Onset": onset, "Nucleus_Coda": nucleus_coda, "Syllabic": True, "Stress": is_stressed})
            elif len(parts) == 2:
                nucleus_coda = parts[1]
                parsed_syllables.append({"Onset": "", "Nucleus_Coda": nucleus_coda, "Syllabic": True, "Stress": is_stressed})
        elif "/" in syllable:
            parts = syllable.split("/")
            if len(parts) == 3:
                onset, nucleus, coda = parts[0], parts[1], parts[2]
                parsed_syllables.append({"Onset": onset, "Nucleus": nucleus, "Coda": coda, "Syllabic": False, "Stress": is_stressed})
            elif len(parts) == 2:
                onset, nucleus, coda = parts[0], parts[1], ""
                parsed_syllables.append({"Onset": onset, "Nucleus": nucleus, "Coda": coda, "Syllabic": False, "Stress": is_stressed})
            else:
                onset, nucleus, coda = "", parts[1], ""
                parsed_syllables.append({"Onset": onset, "Nucleus": nucleus, "Coda": coda, "Syllabic": False, "Stress": is_stressed})
        else:
            parsed_syllables.append({"Onset": "", "Nucleus": "", "Coda": "", "Syllabic": False, "Stress": is_stressed})
    return parsed_syllables

def format_with_slashes(text):
    """Format text with slashes."""
    if text.startswith("/") and text.endswith("/"):
        return text
    return f"/{text}/"

def create_syllable_tree(syllable_data, syllable_number):
    """Create a syllable tree with Graphviz."""
    graph = graphviz.Digraph(format="png")
    syllable_color = "orange" if syllable_data.get("Stress") else "white"

    graph.node(f"Syllable{syllable_number}", "Syllable", shape="ellipse", style="filled", fillcolor=syllable_color)

    if syllable_data.get("Onset"):
        graph.node(f"Onset{syllable_number}", label=f"Onset\n{format_with_slashes(syllable_data['Onset'])}", shape="ellipse")
        graph.edge(f"Syllable{syllable_number}", f"Onset{syllable_number}")

    if syllable_data.get("Syllabic"):
        graph.node(f"Rhyme{syllable_number}", "Rhyme", shape="ellipse")
        graph.edge(f"Syllable{syllable_number}", f"Rhyme{syllable_number}")
        graph.node(f"Nucleus_Coda{syllable_number}", label=f"Nucleus/Coda\n{format_with_slashes(syllable_data['Nucleus_Coda'])}", shape="ellipse")
        graph.edge(f"Rhyme{syllable_number}", f"Nucleus_Coda{syllable_number}")
    else:
        if syllable_data.get("Nucleus"):
            graph.node(f"Nucleus{syllable_number}", label=f"Nucleus\n{format_with_slashes(syllable_data['Nucleus'])}", shape="ellipse")
            graph.edge(f"Syllable{syllable_number}", f"Nucleus{syllable_number}")
        if syllable_data.get("Coda"):
            graph.node(f"Coda{syllable_number}", label=f"Coda\n{format_with_slashes(syllable_data['Coda'])}", shape="ellipse")
            graph.edge(f"Nucleus{syllable_number}", f"Coda{syllable_number}")
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
    st.markdown("""
    ### Instructions:
    1. Enter a **single stressed syllable** using IPA symbols ([Visit IPA online website](https://ipa.typeit.org/)).
    2. Mark stress using `ˈ` before the syllable.
    3. Example: ˈstr/ɛ/ for a stressed syllable.
    """)

    # Input for a single stressed syllable
    syllable_input = st.text_input("Enter a single stressed syllable:", placeholder="e.g., ˈstr/ɛ/")

    def parse_single_syllable(input_syllable):
        """Parse a single stressed syllable into its components."""
        is_stressed = input_syllable.startswith("ˈ")
        if is_stressed:
            input_syllable = input_syllable[1:]  # Remove stress marker

        if "/" in input_syllable:  # Handle regular vowels
            parts = input_syllable.split("/")
            if len(parts) == 3:  # Onset, Nucleus, Coda
                return {"Onset": parts[0], "Nucleus": parts[1], "Coda": parts[2], "Syllabic": False, "Stress": is_stressed}
            elif len(parts) == 2:  # Onset and Nucleus only
                return {"Onset": parts[0], "Nucleus": parts[1], "Coda": "", "Syllabic": False, "Stress": is_stressed}
            elif len(parts) == 1:  # Nucleus only
                return {"Onset": "", "Nucleus": parts[0], "Coda": "", "Syllabic": False, "Stress": is_stressed}
        return {"Onset": "", "Nucleus": "", "Coda": "", "Syllabic": False, "Stress": is_stressed}

    if st.button("Visualize Stressed Syllable"):
        if syllable_input:
            syllable_data = parse_single_syllable(syllable_input)

            if syllable_data and syllable_data.get("Stress"):
                # Create a syllable tree with a yellow circle for stress
                tree = graphviz.Digraph(format="png")
                syllable_color = "yellow" if syllable_data.get("Stress") else "white"

                # Create the main Syllable node
                tree.node(
                    "Syllable", "Syllable", shape="ellipse", style="filled", fillcolor=syllable_color
                )

                # Add the Onset node if present
                if syllable_data.get("Onset"):
                    tree.node(
                        "Onset", f"Onset\n{format_with_slashes(syllable_data['Onset'])}", shape="ellipse"
                    )
                    tree.edge("Syllable", "Onset")

                # Add the Rhyme node
                tree.node("Rhyme", "Rhyme", shape="ellipse")
                tree.edge("Syllable", "Rhyme")

                # Add the Nucleus node
                if syllable_data.get("Nucleus"):
                    tree.node(
                        "Nucleus",
                        f"Nucleus\n{format_with_slashes(syllable_data['Nucleus'])}",
                        shape="ellipse",
                    )
                    tree.edge("Rhyme", "Nucleus")

                # Add the Coda node only if it contains non-whitespace characters
                if syllable_data.get("Coda").strip():  # Check for non-empty Coda
                    tree.node(
                        "Coda",
                        f"Coda\n{format_with_slashes(syllable_data['Coda'])}",
                        shape="ellipse",
                    )
                    tree.edge("Rhyme", "Coda")

                # Display the tree with the appropriate title
                st.markdown(f"### Stressed syllable")
                st.graphviz_chart(tree)
            else:
                st.error("Invalid stressed syllable format. Please try again.")
        else:
            st.error("Please enter a syllable to visualize.")


# Tab 3: Syllable Structure
with tabs[2]:
    st.title("🌳 Syllable Structure Visualizer")
    st.markdown("""
    ### 🔳 Instructions:
    1. Enter a word using IPA symbols ([Visit IPA online website](https://ipa.typeit.org/)).
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
            for i, syl in enumerate(syllables, start=1):
                if syl.get("Onset") or syl.get("Nucleus") or syl.get("Coda") or syl.get("Nucleus_Coda"):
                    st.markdown(f"### Syllable {i}")
                    tree = create_syllable_tree(syl, i)
                    st.graphviz_chart(tree)
        else:
            st.error("Please enter a valid syllabified input.")
