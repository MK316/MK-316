import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("https://drive.google.com/uc?export=download&id=1jS-21_KGT6HtbPvFjBBXHMU7qCDTnCIo")  # Replace with your actual file path

# Define the correct passcode for main app access
correct_passcode = "7722190"
redirect_url = "https://coding4et.streamlit.app/Classapp"  # Page to open upon successful login

def show_passcode_input():
    st.title("Passcode Required")
    st.caption("Enter passcode to access the page")
    # Using a form to handle inputs and button as a single action
    with st.form(key='PasscodeForm'):
        input_passcode = st.text_input("Enter the passcode:", type="password")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            # Check the passcode directly within the form processing
            if input_passcode == correct_passcode:
                st.session_state['authenticated'] = True
            else:
                st.error("You don't seem to have permission!")
                st.session_state['authenticated'] = False

# Initialize the session state for 'authenticated' if it does not exist
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Define function for the dot plot in Tab2
def display_dot_plot():
    # Sort data by Midterm scores in descending order
    sorted_data = data.sort_values(by='Midterm', ascending=False).reset_index(drop=True)
    
    # Set X-axis values from 1 to the length of the data
    sorted_data['X'] = range(1, len(sorted_data) + 1)
    
    # Define colors: top 7 green, next 7 blue, and the rest red
    colors = ['green'] * 7 + ['blue'] * 7 + ['red'] * (len(sorted_data) - 14)
    
    # Create the dot plot
    plt.figure(figsize=(10, 6))
    plt.scatter(sorted_data['X'], sorted_data['Midterm'], color=colors, s=100)
    
    # Add vertical lines at specified positions
    plt.axvline(x=7.5, color='gray', linestyle='--')
    plt.axvline(x=14.5, color='gray', linestyle='--')
    
    # Set limits and labels
    plt.ylim(0, 80)
    plt.xlabel("Rank (1 to 21)")
    plt.ylabel("Midterm Score")
    plt.title("Midterm Scores: Highest to Lowest")
    
    # Display the plot
    st.pyplot(plt)

# Tabs for different sections of the app
tab1, tab2, tab3, tab4 = st.tabs(["Phonology Midterm", "Midterm Score Plot", "Tab 3", "Tab 4"])

# First tab for Midterm score lookup
with tab1:
    # Display the passcode input form or the link based on the authentication status
    if not st.session_state['authenticated']:
        show_passcode_input()
    else:
        st.success("Access Granted")
        
        # Code for Midterm score lookup
        st.subheader("Phonology Midterm Score Lookup")
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

# Second tab for Midterm score dot plot
with tab2:
    st.header("Midterm Score Dot Plot")
    display_dot_plot()
