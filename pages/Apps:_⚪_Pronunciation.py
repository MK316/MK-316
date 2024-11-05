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
tab1, tab2 = st.tabs(["Accuracy Feedback",
