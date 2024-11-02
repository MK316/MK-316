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
    # Text input for passcode and submit button
    input_passcode = st.text_input("Enter the passcode:", type="password")
    submit_button = st.button("Submit")
    
    # Check the passcode when the 'Submit' button is clicked
    if submit_button:
        if input_passcode == correct_passcode:
            st.session_state['authenticated'] = True
            st.success("Access Granted")
        else:
            st.error("You don't seem to have permission!")
            st.session_state['authenticated'] = False

# Initialize the session state for 'authenticated' if it does not exist
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Function to display dot plot of Midterm scores
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

# Function to display boxplot of Midterm scores grouped by Group
def display_group_boxplot():
    plt.figure(figsize=(8, 6))
    data.boxplot(column='Midterm', by='Group', grid=False)
    plt.title("Boxplot of Midterm Scores by Group")
    plt.suptitle("")  # Remove the automatic title to avoid duplication
    plt.xlabel("Group")
    plt.ylabel("Midterm Score")
    st.pyplot(plt)

# Tabs for different sections of the app
tab1, tab2, tab3, tab4 = st.tabs(["Phonology Midterm", "Tab 2", "Tab 3", "Tab 4"])

# First tab for Midterm score lookup and plot buttons
with tab1:
    # Display the passcode input form or the link based on the authentication status
    if not st.session_state['authenticated']:
        show_passcode_input()
    else:
        st.markdown("Try agin", unsafe_allow_html=True)
        
        # Code for Midterm score lookup
        st.subheader("Fall 202: Phonology Midterm Score Lookup")
        user_passcode = st.text_input("Enter your Passcode for Midterm Score:")
        lookup_button = st.button("🙏 Lookup My Score")

        # Check if the passcode is entered and 'Lookup Score' button is clicked
        if lookup_button and user_passcode:
            # Filter data for the entered passcode
            filtered_data = data[data['Passcode'] == user_passcode]

            # Display the Midterm score if the passcode is found
            if not filtered_data.empty:
                midterm_score = filtered_data['Midterm'].values[0]
                st.write(f"Your Midterm score is: {midterm_score} out of 75 points ({(midterm_score/75)*100:.1f}% of accuracy)")
            else:
                st.write("Invalid Passcode for Midterm Score. Please try again.")
        
        # Buttons for additional plots
        if st.button("💫 Show Midterm Score Dot Plot"):
            st.header("Midterm Score Dot Plot")
            display_dot_plot()
        
        if st.button("👪 Show Boxplot of Scores by Group"):
            st.header("Midterm Scores by Group")
            display_group_boxplot()
