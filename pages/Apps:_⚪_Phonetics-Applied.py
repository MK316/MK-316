import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import soundfile as sf
from io import BytesIO

# Title of the app
st.title("Fundamental Frequency (F0) Estimation")

# Step 1: Upload or record audio file (upload for now, Streamlit doesn't have a native audio recorder)
st.header("Upload an audio file")

# Audio file uploader
uploaded_file = st.file_uploader("Upload an audio file in .wav format", type=["wav"])

# Process the uploaded audio file if it's available
if uploaded_file is not None:
    # Load audio data
    audio_bytes = uploaded_file.read()
    st.audio(audio_bytes, format="audio/wav")

    # Save the uploaded file to process it
    audio_data, sr = librosa.load(BytesIO(audio_bytes), sr=None)  # Load without resampling
    
    # Step 2: Compute the fundamental frequency (F0)
    st.header("Processing the audio to estimate F0")
    fmin = 50  # Set the minimum frequency for F0 (e.g., typical human pitch range)
    fmax = 300  # Set the maximum frequency for F0

    # Using librosa.pyin to estimate the F0
    f0, voiced_flag, voiced_probs = librosa.pyin(audio_data, fmin=fmin, fmax=fmax, sr=sr)

    # Plot the fundamental frequency (F0)
    times = librosa.times_like(f0, sr=sr)
    fig, ax = plt.subplots()
    ax.set(title='Fundamental Frequency (F0)')
    ax.plot(times, f0, label='F0 (Fundamental Frequency)', color='r')
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Frequency (Hz)")
    ax.legend()

    # Show the plot
    st.pyplot(fig)

    # Step 3: Display approximate average F0
    if np.any(f0):
        avg_f0 = np.nanmean(f0)  # Use nanmean to avoid NaN values when calculating the average
        st.write(f"Approximate average fundamental frequency (F0): {avg_f0:.2f} Hz")
    else:
        st.write("F0 could not be estimated from the audio.")

else:
    st.write("Please upload a valid .wav audio file to proceed.")
