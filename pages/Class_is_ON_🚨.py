import streamlit as st

# Define the correct passcode
correct_passcode = "1234"
redirect_url = "https://coding4et.streamlit.app/Classapp"  # This URL should be the page you want to open upon successful login

def show_passcode_input():
    st.title("Passcode Required")
    input_passcode = st.text_input("Enter the passcode to access the page:", type="password")
    submit_button = st.button("Submit")
    
    if submit_button:
        if input_passcode == correct_passcode:
            # Mark the session as authenticated
            st.session_state['authenticated'] = True
        else:
            st.error("You don't seem to have permission!")

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    show_passcode_input()
else:
    # Display the link to the page when the passcode is correct
    st.success("Access Granted")
    st.markdown(f"[Proceed to the application]({redirect_url})", unsafe_allow_html=True)
