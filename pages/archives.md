# Play audio (as buttons)

### F0
```
import streamlit as st
import numpy as np
import librosa
import matplotlib.pyplot as plt
from io import BytesIO
import soundfile as sf

# Title of the app
st.title("Your Voice Pitch")
st.caption("Fundamental Frequency (F0) Estimation")
st.write("Record the following sentence and upload the audio in wav format:")

st.markdown("### '_Moments of meaning emerge when we listen to the sound of the heart._'")

# Create two tabs: Upload and View Results
tab1, tab2 = st.tabs(["Upload Audio", "View Results"])

# Step 1: Upload or record audio file
with tab1:
    st.header("Upload an audio file")
    uploaded_file = st.file_uploader("Upload an audio file in .wav format", type=["wav"])
    
    if uploaded_file is not None:
        # Save the uploaded file temporarily
        temp_file_path = "temp_audio_file.wav"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.read())
        
        st.audio(temp_file_path, format="audio/wav")
        
        # Load audio data using librosa
        try:
            audio_data, sr = librosa.load(temp_file_path, sr=None)  # Load without resampling
            
            # Compute the fundamental frequency (F0)
            fmin = 50  # Minimum expected frequency (e.g., typical human pitch range)
            fmax = 300  # Maximum expected frequency

            f0, voiced_flag, voiced_probs = librosa.pyin(audio_data, fmin=fmin, fmax=fmax, sr=sr)

            # Store F0 and other info in session state
            st.session_state['f0'] = f0
            st.session_state['sr'] = sr
            st.session_state['audio_data'] = audio_data
            st.success("Audio processed successfully. Check the 'View Results' tab for details.")

        except Exception as e:
            st.error(f"An error occurred while processing the audio: {e}")

# Step 2: View the Results in tab 2
# Step 2: View the Results in tab 2
with tab2:
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
        
        # Set y-axis limit to display between 0 and 300 Hz
        ax.set_ylim([0, 300])

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
        st.write("No results to display. Please upload and process audio in the previous tab.")

```

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

# Acoustics including spectrogram in hz

```
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
    try:
        y, sr = librosa.load(audio_path, sr=None)
        # Generate a Short-Time Fourier Transform (STFT) spectrogram
        D = np.abs(librosa.stft(y))
        # Convert power spectrogram (amplitude squared) to decibel (dB) units
        S_dB = librosa.amplitude_to_db(D, ref=np.max)

        plt.figure(figsize=(10, 4))
        # We use specshow to display a spectrogram with a linear frequency axis
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='linear', hop_length=512)
        plt.colorbar(format='%+2.0f dB')
        plt.title('Frequency Spectrogram in Hz')
        
        # Apply the user-selected axis limits
        plt.xlim([time_min, time_max])  # Set time axis limits
        plt.ylim([freq_min, freq_max])  # Set frequency axis limits directly in Hz

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


```
# Acoustics including spectrogram (good) 2PM1021

```
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
    tone_int16 = np.int16(tone / np.max(np.abs(tone)) * 32767)  # Convert to 16-bit data
    return tone_int16, t, tone

def plot_spectrogram(audio_path, time_min, time_max, freq_min, freq_max):
    try:
        y, sr = librosa.load(audio_path, sr=None)
        if y.size == 0:
            st.error("Loaded audio is empty. Please check the file and try again.")
            return
        
        start_sample = int(time_min * sr)
        end_sample = int(time_max * sr)

        if start_sample >= end_sample:
            st.error("End time must be greater than start time.")
            return
        if end_sample > len(y):
            st.error("End time exceeds the audio duration.")
            return
        
        y_segment = y[start_sample:end_sample]

        if y_segment.size == 0:
            st.error("Selected audio segment is empty.")
            return

        D = np.abs(librosa.stft(y_segment))
        S_dB = librosa.amplitude_to_db(D, ref=np.max)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='linear', hop_length=512)
        plt.colorbar(format='%+2.0f dB')
        plt.title('Frequency Spectrogram in Hz')
        plt.xlim([0, time_max - time_min])  # Adjust the x-axis to the duration of the segment
        plt.ylim([freq_min, freq_max])
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.tight_layout()
        st.pyplot(plt)

        buffer = BytesIO()
        write(buffer, sr, y_segment.astype(np.int16))
        buffer.seek(0)
        st.audio(buffer, format='audio/wav')

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
        duration_input = st.slider('Duration (seconds):', min_value=0.1, max_value=5.0, value=1.0, step=0.1)
        generate_button = st.button('Generate Tone')

        if generate_button:
            data, t, waveform = generate_tone(freq_input, duration=duration_input)
            buffer = BytesIO()
            write(buffer, 44100, data)
            buffer.seek(0)
            st.audio(buffer, format='audio/wav')

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
            st.audio(audio_path)  # Play the uploaded audio file immediately

            time_min = st.slider('Start Time (s)', min_value=0.0, max_value=30.0, value=0.0, step=0.1)
            time_max = st.slider('End Time (s)', min_value=0.1, max_value=30.0, value=5.0, step=0.1)
            freq_min = st.slider('Min Frequency (Hz)', min_value=0, max_value=8000, value=0, step=100)
            freq_max = st.slider('Max Frequency (Hz)', min_value=1000, max_value=20000, value=8000, step=100)

            if st.button('Generate Spectrogram'):
                plot_spectrogram(audio_path, time_min, time_max, freq_min, freq_max)

if __name__ == "__main__":
    main()

```

# Adding complex wave generator (3PM 10/21)

```
import streamlit as st
import numpy as np
from scipy.io.wavfile import write
from io import BytesIO
import librosa
import librosa.display
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def generate_wave(amplitude, frequency, time):
    """Generate sinusoidal wave data based on amplitude, frequency, and time."""
    return amplitude * np.sin(2 * np.pi * frequency * time)

def generate_tone(frequency, duration=1, sample_rate=44100, amplitude=0.3):
    """Generate a pure tone based on the frequency."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = amplitude * np.sin(2 * np.pi * frequency * t)
    tone_int16 = np.int16(tone / np.max(np.abs(tone)) * 32767)  # Convert to 16-bit data
    return tone_int16, t, tone

def plot_spectrogram(audio_path, time_min, time_max, freq_min, freq_max):
    try:
        y, sr = librosa.load(audio_path, sr=None)
        if y.size == 0:
            st.error("Loaded audio is empty. Please check the file and try again.")
            return
        
        start_sample = int(time_min * sr)
        end_sample = int(time_max * sr)

        if start_sample >= end_sample:
            st.error("End time must be greater than start time.")
            return
        if end_sample > len(y):
            st.error("End time exceeds the audio duration.")
            return
        
        y_segment = y[start_sample:end_sample]

        if y_segment.size == 0:
            st.error("Selected audio segment is empty.")
            return

        D = np.abs(librosa.stft(y_segment))
        S_dB = librosa.amplitude_to_db(D, ref=np.max)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='linear', hop_length=512)
        plt.colorbar(format='%+2.0f dB')
        plt.title('Frequency Spectrogram in Hz')
        plt.xlim([0, time_max - time_min])  # Adjust the x-axis to the duration of the segment
        plt.ylim([freq_min, freq_max])
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.tight_layout()
        st.pyplot(plt)

        buffer = BytesIO()
        write(buffer, sr, y_segment.astype(np.int16))
        buffer.seek(0)
        st.audio(buffer, format='audio/wav')

    except Exception as e:
        st.error(f"An error occurred while generating the spectrogram: {str(e)}")


def main():
    st.title('Acoustics')
    tabs = st.tabs(["Introduction", "Generate Tone", "Upload and Analyze Spectrogram","Complex wave"])

    with tabs[0]:
        st.write("Welcome to the Acoustics module. This module allows you to explore various aspects of sound.")

    with tabs[1]:
        st.write("Generate a pure tone based on a specified frequency.")
        freq_input = st.number_input('Enter a frequency (50 to 500 Hz):', min_value=50, max_value=500, value=100, step=1)
        duration_input = st.slider('Duration (seconds):', min_value=0.1, max_value=5.0, value=1.0, step=0.1)
        generate_button = st.button('Generate Tone')

        if generate_button:
            data, t, waveform = generate_tone(freq_input, duration=duration_input)
            buffer = BytesIO()
            write(buffer, 44100, data)
            buffer.seek(0)
            st.audio(buffer, format='audio/wav')

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
            st.audio(audio_path)  # Play the uploaded audio file immediately

            time_min = st.slider('Start Time (s)', min_value=0.0, max_value=30.0, value=0.0, step=0.1)
            time_max = st.slider('End Time (s)', min_value=0.1, max_value=30.0, value=5.0, step=0.1)
            freq_min = st.slider('Min Frequency (Hz)', min_value=0, max_value=8000, value=0, step=100)
            freq_max = st.slider('Max Frequency (Hz)', min_value=1000, max_value=20000, value=8000, step=100)

            if st.button('Generate Spectrogram'):
                plot_spectrogram(audio_path, time_min, time_max, freq_min, freq_max)

    with tabs[3]:
        st.subheader("Generate a Complex Wave")
        col1, col2 = st.columns(2)
        amp1 = col1.number_input('Amplitude of Wave 1:', value=1.0, format="%.2f")
        freq1 = col2.number_input('Frequency of Wave 1:', value=1.0, format="%.2f")
        
        amp2 = col1.number_input('Amplitude of Wave 2:', value=1.0, format="%.2f")
        freq2 = col2.number_input('Frequency of Wave 2:', value=1.0, format="%.2f")
        
        amp3 = col1.number_input('Amplitude of Wave 3:', value=1.0, format="%.2f")
        freq3 = col2.number_input('Frequency of Wave 3:', value=1.0, format="%.2f")
        
        t_max = st.slider("Select max time for the x-axis:", min_value=1, max_value=10, value=5, step=1)
        
        if st.button('Generate a complex wave'):
            time = np.linspace(0, t_max, 1000)
            wave1 = generate_wave(amp1, freq1, time)
            wave2 = generate_wave(amp2, freq2, time)
            wave3 = generate_wave(amp3, freq3, time)
            complex_wave = wave1 + wave2 + wave3

            plt.figure(figsize=(10, 4))
            plt.plot(time, wave1, label="Wave 1", linestyle='--')
            plt.plot(time, wave2, label="Wave 2", linestyle='--')
            plt.plot(time, wave3, label="Wave 3", linestyle='--')
            plt.plot(time, complex_wave, label="Complex Wave", linewidth=2)
            plt.title("Complex Wave Formation")
            plt.xlabel("Time")
            plt.ylabel("Amplitude")
            plt.legend()
            st.pyplot(plt)
if __name__ == "__main__":
    main()

```
