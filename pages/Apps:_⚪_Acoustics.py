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

def plot_spectrogram(audio_path, time_min, time_max, freq_min, freq_max):
    """Load an audio file and plot its spectrogram."""
    try:
        y, sr = librosa.load(audio_path, sr=None)
        S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
        S_dB = librosa.power_to_db(S, ref=np.max)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Mel-frequency Spectrogram')
        plt.xlim(time_min, time_max)
        plt.ylim(librosa.hz_to_mel(freq_min), librosa.hz_to_mel(freq_max))
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
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

            time_min = st.slider('Start Time (s)', min_value=0.0, max_value=10.0, value=0.0, step=0.1)
            time_max = st.slider('End Time (s)', min_value=0.0, max_value=10.0, value=10.0, step=0.1)
            freq_min = st.slider('Min Frequency (Hz)', min_value=0, max_value=8000, value=0, step=100)
            freq_max = st.slider('Max Frequency (Hz)', min_value=1000, max_value=20000, value=8000, step=100)

            if st.button('Generate Spectrogram'):
                plot_spectrogram(audio_path, time_min, time_max, freq_min, freq_max)

if __name__ == "__main__":
    main()
