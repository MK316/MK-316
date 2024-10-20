import streamlit as st
import parselmouth
import numpy as np
import plotly.express as px
from streamlit_audio_recorder import st_audio_recorder

def analyze_formants(audio_file):
    sound = parselmouth.Sound(audio_file)
    formant = sound.to_formant_burg()
    f1 = formant.get_value_at_time(1, 0.5)  # Get F1 at midpoint of the sound
    f2 = formant.get_value_at_time(2, 0.5)  # Get F2 at midpoint of the sound
    return f1, f2

def main():
    st.title('Acoustics')
    tabs = st.tabs(["Introduction", "Generate Tone", "Record Vowels", "Tab 4"])

    with tabs[2]:
        st.header("Record and Analyze Vowels")
        st.write("Record four vowels and analyze their formant frequencies.")

        # Record audio
        audio_data = st_audio_recorder(recorder_id="vowel_recorder", time_limit=5000)
        
        if audio_data["recording"]:
            # Save the recording
            with open("temp_audio.wav", "wb") as f:
                f.write(audio_data["recording"])
            st.success("Recording saved!")

        analyze_button = st.button('Analyze Vowels')
        if analyze_button and "temp_audio.wav":
            # Perform analysis
            f1, f2 = analyze_formants("temp_audio.wav")
            # Plot formants
            formants = {"Vowels": ["Vowel"], "F1": [f1], "F2": [f2]}
            fig = px.scatter(formants, x="F1", y="F2", text="Vowels", labels={"F1": "Formant 1 (Hz)", "F2": "Formant 2 (Hz)"})
            fig.update_traces(textposition='top center')
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
