import streamlit as st
import numpy as np
from scipy.io.wavfile import write
from io import BytesIO
import librosa
import librosa.display
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def generate_tone(frequency, duration=1, sample_rate=44100, amplitude=0.3):
    """Generate a pure tone based on the frequency."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = amplitude * np.sin(2 * np.pi * frequency * t)
    return np.int16(tone / np.max(np.abs(tone)) * 32767), t, tone

def plot_spectrogram(audio_path, n_mels, hop_length):
    """Load an audio file and plot its spectrogram."""
    try:
        y, sr = librosa.load(audio_path, sr=None)
        # Ensure all parameters are passed as keyword arguments
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, hop_length=hop_length)
        S_dB = librosa.power_to_db(S, ref=np.max)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Mel-frequency Spectrogram')
        plt.tight_layout()
        st.pyplot(plt)
    except Exception as e:
        st.error(f"An error occurred while generating the spectrogram: {str(e)}")

def main():
    st.title('Acoustics')
    tabs = st.tabs(["Introduction", "Generate Tone", "Upload and Analyze Spectrogram"])

    with tabs[0]:
        st.write("Welcome to the Acoustics module. This module allows you to explore various aspects of sound.")

    with tabs[1]:
        st.write("Generate a pure tone based on a specified frequency.")
        freq_input = st.number_input('Enter a frequency (50 to 500 Hz):', min_value=50, max_value=500, value=100, step=1)
        generate_button = st.button('Generate Tone')

        if generate_button:
            data, t, waveform = generate_tone(freq_input)
            buffer = BytesIO()
            write(buffer, 44100, data)
            buffer.seek(0)
            st.audio(buffer, format='audio/wav', start_time=0)

            fig = go.Figure(data=go.Scatter(x=t, y=waveform))
            fig.update_layout(
                title=f"Waveform of the Generated Tone at {freq_input} Hz",
                xaxis_title='Time [s]',
                yaxis_title='Amplitude',
                xaxis_rangeslider_visible=True
            )
            st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:
        st.header("Upload and Analyze Spectrogram")
        uploaded_file = st.file_uploader("Upload your audio file (WAV format)", type=['wav'])

        if uploaded_file is not None:
            audio_path = 'temp_audio.wav'
            with open(audio_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            st.success("File uploaded successfully!")

            n_mels = st.slider('Number of Mel Bands', min_value=16, max_value=256, value=128, step=16)
            hop_length = st.slider('Hop Length', min_value=256, max_value=2048, value=512, step=128)

            if st.button('Generate Spectrogram'):
                plot_spectrogram(audio_path, n_mels=n_mels, hop_length=hop_length)

if __name__ == "__main__":
    main()
