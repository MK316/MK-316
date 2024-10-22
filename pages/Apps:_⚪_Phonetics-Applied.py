import streamlit as st
import numpy as np
import librosa
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import soundfile as sf
from io import BytesIO

# Title of the app
st.title("Fundamental Frequency (F0) Estimation")

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs(["Upload Audio", "Process Audio", "View Results"])

# Step 1: Upload or record audio file
with tab1:
    st.header("Upload an audio file")
    uploaded_file = st.file_uploader("Upload an audio file in .wav format", type=["wav"])
    
    if uploaded_file is not None:
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes, format="audio/wav")
        
        # Store uploaded file in session state
        st.session_state['uploaded_file'] = uploaded_file

# Step 2: Process the uploaded audio file (in tab 2)
with tab2:
    st.header("Processing the audio to estimate F0")
    
    if 'uploaded_file' in st.session_state:
        uploaded_file = st.session_state['uploaded_file']
        
        # Load audio data
        audio_data, sr = librosa.load(BytesIO(uploaded_file.read()), sr=None)  # Load without resampling
        
        # Compute the fundamental frequency (F0)
        fmin = 50  # Minimum expected frequency (e.g., typical human pitch range)
        fmax = 300  # Maximum expected frequency

        f0, voiced_flag, voiced_probs = librosa.pyin(audio_data, fmin=fmin, fmax=fmax, sr=sr)

        # Store F0 and other info in session state
        st.session_state['f0'] = f0
        st.session_state['sr'] = sr
        st.session_state['audio_data'] = audio_data
    else:
        st.write("Please upload a valid .wav audio file in the first tab to proceed.")

# Step 3: View the Results in tab 3
with tab3:
    st.header("Results")

    if 'f0' in st.session_state:
        f0 = st.session_state['f0']
        sr = st.session_state['sr']

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

        # Display approximate average F0
        if np.any(f0):
            avg_f0 = np.nanmean(f0)  # Use nanmean to avoid NaN values when calculating the average
            st.write(f"Approximate average fundamental frequency (F0): {avg_f0:.2f} Hz")
        else:
            st.write("F0 could not be estimated from the audio.")
    else:
        st.write("No results to display. Please upload and process audio in the previous tabs.")
