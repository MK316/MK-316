import streamlit as st
import numpy as np
from scipy.io.wavfile import write
from io import BytesIO
import matplotlib.pyplot as plt

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

            # Plotting the waveform
            fig, ax = plt.subplots()
            ax.plot(t, waveform)
            ax.set_title(f"Waveform of the Generated Tone at {freq_input} Hz")
            ax.set_xlabel('Time [s]')
            ax.set_ylabel('Amplitude')
            st.pyplot(fig)

    with tabs[2]:
        st.write("Details for Tab 3 will go here.")

    with tabs[3]:
        st.write("Details for Tab 4 will go here.")

if __name__ == "__main__":
    main()
