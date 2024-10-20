import streamlit as st
import webbrowser

# Define the correct passcode
correct_passcode = "1234"
redirect_url = "https://huggingface.co/spaces/MK-316/mytimer"  # This URL should be the page you want to open upon successful login

def show_passcode_input():
    st.title("Passcode Required")
    input_passcode = st.text_input("Enter the passcode to access the page:", type="password")
    submit_button = st.button("Submit")
    
    if submit_button:
        if input_passcode == correct_passcode:
            # Open a new page if the passcode is correct
            webbrowser.open_new_tab(redirect_url)
        else:
            st.error("You don't seem to have permission!")

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    show_passcode_input()
else:
    # Optionally handle other content, but normally this would not execute as we redirect on success
    st.write("You are already authenticated!")
