import streamlit as st

# Define the correct passcode
correct_passcode = "1234"

# Function to display the main content of the page
def main_content():
    st.title("This is a protected Page, as I use personal data for apps.")
    st.write("Explore other pages :-)")

# Check if 'passcode' is in the session state (persistent between reruns)
if 'passcode' not in st.session_state:
    st.session_state['passcode'] = None  # Initialize it with None

# Create a passcode input field
input_passcode = st.text_input("Enter the passcode to access the page:", type="password")

# Button to submit the passcode
if st.button("Submit"):
    if input_passcode == correct_passcode:
        st.session_state['passcode'] = input_passcode  # Set the session state
        main_content()  # Display the main content if passcode is correct
    else:
        st.error("Incorrect passcode, please try again.")

# If the passcode in session state is correct, directly display the content
if st.session_state['passcode'] == correct_passcode:
    main_content()
