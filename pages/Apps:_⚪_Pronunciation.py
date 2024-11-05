import streamlit as st
import speech_recognition as sr
from Levenshtein import ratio
import tempfile
import numpy as np
import soundfile as sf
import pandas as pd

# Sample dataframe with sentences
data = {
    "Sentences": [
        "A stitch in time saves nine.",
        "To be or not to be, that is the question.",
        "Five cats were living in safe caves.",
        "Hives give shelter to bees in large caves.",
        "His decision to plant a rose was amazing.",
        "She sells sea shells by the sea shore.",
        "The colorful parrot likes rolling berries.",
        "Time flies like an arrow; fruit flies like a banana.",
        "Good things come to those who wait.",
        "All human beings are born free and equal in dignity and rights."
    ]
}
df = pd.DataFrame(data)
user_scores = {}

# Function to transcribe audio
def transcribe_audio(file_path):
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"

# Function to calculate pronunciation correction
def pronunciation_correction(name, expected_text, audio_file):
    user_spoken_text = transcribe_audio(audio_file)
    similarity = ratio(expected_text.lower(), user_spoken_text.lower())
    score = float(f"{similarity:.2f}")
    
    if name in user_scores:
        user_scores[name].append(score)
    else:
        user_scores[name] = [score]
    
    feedback = "Excellent pronunciation!" if score >= 0.9 else \
               "Good pronunciation!" if score >= 0.7 else \
               "Needs improvement." if score >= 0.5 else \
               "Poor pronunciation, try to focus more on clarity."
    return feedback, score

# Function to calculate average score
def calculate_average(name):
    if name in user_scores and user_scores[name]:
        filtered_scores = [score for score in user_scores[name] if score > 0]  # Ignore zeros
        average_score = sum(filtered_scores) / len(filtered_scores)
    else:
        average_score = 0
    return f"Great job, {name}! Your average score is: {average_score:.2f}. Keep practicing to improve further!"

# Streamlit app layout
st.title("Pronunciation Accuracy Feedback App")

# Tabs
tab1, tab2, tab3 = st.tabs(["Accuracy Feedback", "Recording", "More apps"])

# Tab 1: Accuracy Feedback
with tab1:
    st.subheader("Check Your Pronunciation Accuracy")
    
    # User inputs
    name = st.text_input("Enter your name", placeholder="Type your name here...")
    sentence = st.selectbox("Select a Sentence", df['Sentences'].tolist())
    st.write("Selected Sentence:", sentence)
    
    # Audio upload
    audio_file = st.file_uploader("Upload your audio file (WAV format)", type=["wav"])

    # Button to check pronunciation
    if st.button("Check Pronunciation"):
        if name and audio_file and sentence:
            with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as tmpfile:
                tmpfile.write(audio_file.read())
                tmpfile.seek(0)
                feedback, score = pronunciation_correction(name, sentence, tmpfile.name)
                st.write("Pronunciation Feedback:", feedback)
                st.write("Pronunciation Accuracy Score:", score)
        else:
            st.warning("Please enter your name, select a sentence, and upload an audio file.")
    
    # Button to show average score
    if st.button("Show Average Score"):
        if name:
            avg_score = calculate_average(name)
            st.write(avg_score)
        else:
            st.warning("Please enter your name to calculate the average score.")

# Tab 2: Recording
with tab2:
    st.subheader("Audio Recorder")
    st.write("Click the record button below to capture your speech.")

    audio_bytes = st.audio(st.file_uploader("Upload or record audio here"), format="audio/wav")
    if audio_bytes:
        st.audio(audio_bytes, format='audio/wav')
        st.write("Recording uploaded successfully!")

# Tab 3: More apps placeholder
with tab3:
    st.subheader("More Apps")
    st.write("To be updated")
