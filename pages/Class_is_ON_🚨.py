import streamlit as st

# Define the correct passcode
correct_passcode = "1234"

def main_content():
    st.title("Protected Page")
    tab1, tab2, tab3 = st.tabs(["Home", "Data", "Settings"])

    with tab1:
        st.header("Home")
        st.write("Welcome to the home page!")

    with tab2:
        st.header("Data")
        st.write("Here you can view data.")

    with tab3:
        st.header("Settings")
        st.write("Adjust your settings here.")

# Initialize session state for passcode if not already present
if 'passcode' not in st.session_state:
    st.session_state['passcode'] = None

# Handle passcode input and verification
def check_passcode():
    input_passcode = st.text_input("Enter the passcode to access the page:", type="password", key="passcode_input")
    submit_button = st.button("Submit")

    if submit_button:
        if input_passcode == correct_passcode:
            st.session_state['passcode'] = input_passcode  # Update session state to correct passcode
            st.experimental_rerun()  # Rerun the script to refresh the page and display the main content
        else:
            st.error("Incorrect passcode, please try again.")

# Display passcode input or main content based on the passcode verification
if st.session_state['passcode'] == correct_passcode:
    main_content()
else:
    check_passcode()
