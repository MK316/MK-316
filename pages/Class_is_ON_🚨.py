import streamlit as st

# Define the correct passcode
correct_passcode = "1234"
redirect_url = "https://coding4et.streamlit.app/Classapp"  # This URL should be the page you want to open upon successful login

def show_passcode_input():
    st.title("Passcode Required")
    # Using a form to handle inputs and button as a single action
    with st.form(key='PasscodeForm'):
        input_passcode = st.text_input("Enter the passcode to access the page:", type="password")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            # Check the passcode directly within the form processing
            if input_passcode == correct_passcode:
                # Directly update the session state to True if passcode is correct
                st.session_state['authenticated'] = True
            else:
                st.error("You don't seem to have permission!")
                # Reset the session state to False if the passcode is incorrect
                st.session_state['authenticated'] = False

# Initialize the session state for 'authenticated' if it does not exist
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Display the passcode input form or the link based on the authentication status
if not st.session_state['authenticated']:
    show_passcode_input()
else:
    st.success("Access Granted")
    st.markdown(f"[Proceed to the Application]({redirect_url})", unsafe_allow_html=True)
