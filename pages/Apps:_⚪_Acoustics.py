import streamlit as st
import numpy as np
from scipy.io.wavfile import write, read
from io import BytesIO
import plotly.graph_objects as go
import librosa
import librosa.display
import matplotlib.pyplot as plt

def generate_tone(frequency, duration=1, sample_rate=44100, amplitude=0.3):
    """Generate a pure tone based on the frequency."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = amplitude * np.sin(2 * np.pi * frequency * t)
    return np.int16(tone / np.max(np.abs(tone)) * 32767), t, tone

def plot_spectrogram(audio_path):
    """Load an audio file and plot its spectrogram."""
    try:
        y, sr = librosa.load(audio_path, sr=None)  # Use the original sampling rate
        S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
        S_dB = librosa.power_to_db(S, ref=np.max)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Mel-frequency spectrogram')
        plt.tight_layout()
        st.pyplot(plt)  # Display the plot in Streamlit
    except Exception as e:
        st.error(f"An error occurred while generating spectrogram: {e}")

def main():
    st.title('Acoustics')
    tabs = st.tabs(["Introduction", "Generate Tone", "Tab 3", "Upload and Analyze Spectrogram"])

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
            st.session_state['audio_buffer'] = buffer
            st.session_state['waveform_data'] = (t, waveform)
            st.session_state['freq_input'] = freq_input

        if 'audio_buffer' in st.session_state:
            st.audio(st.session_state['audio_buffer'], format='audio/wav', start_time=0)

        if 'waveform_data' in st.session_state:
            display_waveform_button = st.button('Display Waveform')
            if display_waveform_button:
                t, waveform = st.session_state['waveform_data']
                fig = go.Figure(data=go.Scatter(x=t, y=waveform))
                fig.update_layout(
                    title=f"Waveform of the Generated Tone at {st.session_state['freq_input']} Hz",
                    xaxis_title='Time [s]',
                    yaxis_title='Amplitude',
                    xaxis_rangeslider_visible=True
                )
                st.plotly_chart(fig, use_container_width=True)

    with tabs[3]:
        st.header("Upload and Analyze Spectrogram")
        uploaded_file = st.file_uploader("Upload your audio file (WAV format)", type=['wav'])

        if uploaded_file is not None:
            audio_path = 'temp_audio.wav'
            with open(audio_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            st.success("File uploaded successfully!")
            plot_spectrogram(audio_path)

if __name__ == "__main__":
    main()
