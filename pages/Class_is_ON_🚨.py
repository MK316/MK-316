import streamlit as st
import pandas as pd

# Load data from CSV file
data = pd.read_csv("your_file.csv")  # Replace with your actual file path

# Define the correct passcode for main app access
correct_passcode = "1234"
redirect_url = "https://coding4et.streamlit.app/Classapp"  # Page to open upon successful login

def show_passcode_input():
    st.title("Passcode Required")
    st.caption("Click the button TWICE to see the page")
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

# Tabs for different sections of the app
tab1, tab2, tab3, tab4 = st.tabs(["Midterm Lookup", "Tab 2", "Tab 3", "Tab 4"])

# First tab for Midterm score lookup
with tab1:
    # Display the passcode input form or the link based on the authentication status
    if not st.session_state['authenticated']:
        show_passcode_input()
    else:
        st.success("Access Granted")
        st.markdown(f"[Proceed to the Application]({redirect_url})", unsafe_allow_html=True)
        
        # Code for Midterm score lookup
        st.subheader("Midterm Score Lookup")
        user_passcode = st.text_input("Enter your Passcode for Midterm Score:")

        # Check if the passcode is entered
        if user_passcode:
            # Filter data for the entered passcode
            filtered_data = data[data['Passcode'] == user_passcode]

            # Display the Midterm score if the passcode is found
            if not filtered_data.empty:
                midterm_score = filtered_data['Midterm'].values[0]
                st.write(f"Your Midterm score is: {midterm_score}")
            else:
                st.write("Invalid Passcode for Midterm Score. Please try again.")
