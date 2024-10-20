import streamlit as st

# Define the correct passcode
correct_passcode = "1234"

# Function to display the main content of the page
def main_content():
    st.caption("Protected Page")
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

# Initialize passcode in session state if not already present
if 'passcode' not in st.session_state:
    st.session_state['passcode'] = None

# Create a passcode input field if the correct passcode hasn't been entered yet
if st.session_state['passcode'] != correct_passcode:
    input_passcode = st.text_input("Enter the passcode to access the page:", type="password")
    submit_button = st.button("Submit")

    if submit_button:
        if input_passcode == correct_passcode:
            st.session_state['passcode'] = input_passcode  # Update session state to correct passcode
            main_content()  # Display the main content if passcode is correct
        else:
            st.error("Incorrect passcode, please try again.")
else:
    # Display the content directly if passcode is already correct
    main_content()
