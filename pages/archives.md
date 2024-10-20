# Play audio (as buttons)
```
import streamlit as st

def phonetics_apps_page():
    st.title('🐾Play sound Apps')
    st.write('Applications used to teach Phonetics.')

    # Describing your apps briefly
    st.markdown("""
    Here is a selection of applications designed to enhance phonetics learning through interactive and innovative tools. These apps provide resources and exercises to improve pronunciation, listening skills, and phonetic awareness.
    """)

    # First row with three columns
    col1, col2, col3 = st.columns(3)  # Define columns for the first row

    with col1:
        st.image("images/button03.png", width=100)
        if st.button('App 2: Playsound', key='2'):
            st.markdown("🌀[App link](https://playsound.streamlit.app/): Upload audio to play; Speed controller", unsafe_allow_html=True)
            st.markdown("2024.10.14")
    
    with col2:
        st.image("images/button03.png", width=100)
        if st.button('App 6: MP3-to-wav', key='6'):
            st.markdown("🌀[App link](https://mk-316-mp3towav.hf.space/): Convert mp3 to wav file", unsafe_allow_html=True)
            st.markdown("2024.10.15")
            
phonetics_apps_page()

# URL to the raw image on GitHub
image_url = "https://github.com/MK316/MK-316/raw/main/images/bg2.png"
# Display the image
st.image(image_url, caption="\"He who knows no foreign languages knows nothing of his own.\" — Johann Wolfgang von Goethe", use_column_width=True)

```

# Acoustics (10/21 6AM)
```
import streamlit as st
import numpy as np
from scipy.io.wavfile import write
from io import BytesIO
import plotly.graph_objects as go

def generate_tone(frequency, duration=1, sample_rate=44100, amplitude=0.3):
    """Generate a pure tone based on the frequency."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = amplitude * np.sin(2 * np.pi * frequency * t)  # Adjust amplitude here
    return np.int16(tone / np.max(np.abs(tone)) * 32767), t, tone

def main():
    st.title('Acoustics')
    tabs = st.tabs(["Introduction", "Generate Tone", "Tab 3", "Tab 4"])

    with tabs[0]:
        st.write("Welcome to the Acoustics module. This module allows you to explore various aspects of sound.")

    with tabs[1]:
        st.write("Generate a pure tone based on a specified frequency.")
        freq_input = st.number_input('Enter a frequency (50 to 500 Hz):', min_value=50, max_value=500, value=100, step=1)
        generate_button = st.button('Generate Tone')

        if generate_button:
            data, t, waveform = generate_tone(freq_input)
            # Write to a buffer
            buffer = BytesIO()
            write(buffer, 44100, data)
            buffer.seek(0)
            st.audio(buffer, format='audio/wav', start_time=0)

            # Plotting the waveform using Plotly
            fig = go.Figure(data=go.Scatter(x=t, y=waveform))
            fig.update_layout(
                title=f"Waveform of the Generated Tone at {freq_input} Hz",
                xaxis_title='Time [s]',
                yaxis_title='Amplitude',
                xaxis_rangeslider_visible=True  # This enables the range slider for x-axis
            )
            st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:
        st.write("Details for Tab 3 will go here.")

    with tabs[3]:
        st.write("Details for Tab 4 will go here.")

if __name__ == "__main__":
    main()

```

# Acoustics code (including displaying spectrogram)
```
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
        # Generate a Mel-scaled spectrogram
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
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


```
