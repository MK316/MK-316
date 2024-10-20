import streamlit as st
import librosa
import librosa.display
import plotly.graph_objects as go
import numpy as np

def plot_spectrogram(audio_path, hop_length=512, n_mels=128):
    """Load an audio file, compute the spectrogram, and plot it using Plotly."""
    y, sr = librosa.load(audio_path, sr=None)  # Use the original sampling rate
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=n_mels, hop_length=hop_length)
    S_dB = librosa.power_to_db(S, ref=np.max)

    # Creating a time vector for the x-axis
    time = np.linspace(0, len(y) / sr, num=S.shape[1])

    # Creating a frequency vector for the y-axis
    mel = librosa.mel_frequencies(n_mels=n_mels, fmin=0, fmax=sr/2)

    # Plot using Plotly
    fig = go.Figure(data=go.Heatmap(
        x=time,
        y=mel,
        z=S_dB,
        colorscale='Viridis'
    ))

    fig.update_layout(
        title='Mel-frequency Spectrogram',
        xaxis=dict(title='Time [sec]'),
        yaxis=dict(title='Frequency [Hz]'),
        yaxis_type='log',  # Log scale for better visualization of frequencies
    )

    st.plotly_chart(fig, use_container_width=True)

def main():
    st.title('Interactive Spectrogram Viewer')
    uploaded_file = st.file_uploader("Upload your audio file", type=['wav', 'mp3'])

    if uploaded_file is not None:
        audio_path = 'temp_audio.wav'
        with open(audio_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")

        # Sliders for dynamic control
        hop_length = st.slider('Select Hop Length', min_value=256, max_value=2048, value=512, step=128)
        n_mels = st.slider('Select Number of Mel Bands', min_value=64, max_value=256, value=128, step=16)

        plot_spectrogram(audio_path, hop_length=hop_length, n_mels=n_mels)

if __name__ == "__main__":
    main()
