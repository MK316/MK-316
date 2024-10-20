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

# Initialize session state for authentication if not already present
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Display passcode input if not authenticated, otherwise show main content
if not st.session_state['authenticated']:
    with st.form("passcode_form"):
        input_passcode = st.text_input("Enter the passcode to access the page:", type="password")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if input_passcode == correct_passcode:
                st.session_state['authenticated'] = True
                # Re-display the page with main content after authentication
                main_content()
            else:
                st.error("Incorrect passcode, please try again.")
else:
    main_content()
