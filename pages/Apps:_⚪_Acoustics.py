import streamlit as st
import numpy as np
from scipy.io.wavfile import write
from io import BytesIO

def generate_tone(frequency, duration=1, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    return np.int16(tone / np.max(np.abs(tone)) * 32767)

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
            # Generate and display the tone
            data = generate_tone(freq_input)
            # Write to a buffer
            buffer = BytesIO()
            write(buffer, 44100, data)
            buffer.seek(0)
            st.audio(buffer, format='audio/wav', start_time=0)

    with tabs[2]:
        st.write("Details for Tab 3 will go here.")

    with tabs[3]:
        st.write("Details for Tab 4 will go here.")

if __name__ == "__main__":
    main()
