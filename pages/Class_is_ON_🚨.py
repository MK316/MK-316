import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV files
data = pd.read_csv("https://drive.google.com/uc?export=download&id=1jS-21_KGT6HtbPvFjBBXHMU7qCDTnCIo")
data2 = pd.read_csv("https://drive.google.com/uc?export=download&id=1pmKIKIr36kRzewdfVGTd8EnS8xVQWute")

# Define the correct passcode for main app access
correct_passcode = "7722190"
redirect_url = "https://mk316home.streamlit.app/Classapp"

def show_passcode_input(tab_key):
    st.title("Passcode Required")
    st.caption("Enter passcode to access the page")
    input_passcode = st.text_input("Enter the passcode:", type="password", key=f"{tab_key}_passcode_input")
    submit_button = st.button("Submit", key=f"{tab_key}_submit_button")
    
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

# Function to determine the percentile category
def calculate_percentile_category(score, scores):
    rank = (scores > score).sum() + 1  # Rank in ascending order
    percentile = (rank / len(scores)) * 100
    
    if percentile <= 10:
        return "Top 10%"
    elif percentile <= 20:
        return "Top 10-20%"
    elif percentile <= 30:
        return "Top 20-30%"
    elif percentile <= 40:
        return "Top 30-40%"
    elif percentile <= 50:
        return "Top 40-50%"
    elif percentile <= 60:
        return "Below the Top 50%"
    elif percentile <= 70:
        return "Below the Top 60%"
    else:
        return "Below the Top 70%"

# Function to display dot plot of Midterm scores for the given dataset
def display_dot_plot(data):
    sorted_data = data.sort_values(by='Midterm', ascending=False).reset_index(drop=True)
    sorted_data['X'] = range(1, len(sorted_data) + 1)
    colors = ['green'] * 7 + ['blue'] * 7 + ['red'] * (len(sorted_data) - 14)

    plt.figure(figsize=(10, 6))
    plt.scatter(sorted_data['X'], sorted_data['Midterm'], color=colors, s=100)
    plt.axvline(x=7.5, color='gray', linestyle='--')
    plt.axvline(x=14.5, color='gray', linestyle='--')
    plt.ylim(0, 80)
    plt.xlabel("Rank (1 to 21)")
    plt.ylabel("Midterm Score")
    plt.title("Midterm Scores: Highest to Lowest")
    st.pyplot(plt)

# Function to display boxplot of Midterm scores grouped by Group for the given dataset
def display_group_boxplot(data):
    plt.figure(figsize=(8, 6))
    data.boxplot(column='Midterm', by='Group', grid=False)
    plt.title("Boxplot of Midterm Scores by Group")
    plt.suptitle("")
    plt.xlabel("Group")
    plt.ylabel("Midterm Score")
    st.pyplot(plt)

# Tabs for different sections of the app
tab1, tab2, tab3, tab4 = st.tabs(["Phonology Midterm", "Phonetics", "Tab 3", "Tab 4"])

# First tab for Phonology Midterm score lookup and plot buttons
with tab1:
    if not st.session_state['authenticated']:
        show_passcode_input("tab1")
    else:
        st.subheader("Fall 202: Phonology Midterm Score Lookup")
        user_passcode = st.text_input("Enter your Passcode for Midterm Score:", key="tab1_user_passcode")
        lookup_button = st.button("🙏 Lookup My Score", key="tab1_lookup_button")

        if lookup_button and user_passcode:
            filtered_data = data[data['Passcode'] == user_passcode]
            if not filtered_data.empty:
                midterm_score = filtered_data['Midterm'].values[0]
                mean_score = data['Midterm'].mean()
                median_score = data['Midterm'].median()
                percentile_category = calculate_percentile_category(midterm_score, data['Midterm'])

                st.write(f"Your Phonology Midterm score is: {midterm_score} out of 75 points ({(midterm_score/75)*100:.1f}% accuracy)")
                st.write(f"Class Average (Mean): {mean_score:.2f}")
                st.write(f"Class Median: {median_score:.2f}")
                st.write(f"Your Performance Category: {percentile_category}")
                
            else:
                st.write("Invalid Passcode for Midterm Score. Please try again.")
        
        if st.button("💫 Show Midterm Score Dot Plot", key="tab1_dotplot_button"):
            st.header("Midterm Score Dot Plot")
            display_dot_plot(data)
        
        if st.button("👪 Show Boxplot of Scores by Group", key="tab1_boxplot_button"):
            st.header("Midterm Scores by Group")
            display_group_boxplot(data)

# Second tab for Phonetics score lookup and plot buttons using data2
with tab2:
    if not st.session_state['authenticated']:
        show_passcode_input("tab2")
    else:
        st.subheader("Phonetics Midterm Score Lookup")
        user_passcode = st.text_input("Enter your Passcode for Phonetics Midterm Score:", key="tab2_user_passcode")
        lookup_button = st.button("🔍 Lookup My Score (Phonetics)", key="tab2_lookup_button")

        if lookup_button and user_passcode:
            filtered_data2 = data2[data2['Passcode'] == user_passcode]
            
            if not filtered_data2.empty:
                midterm_score2 = filtered_data2['Midterm'].values[0]
                mean_score = data2['Midterm'].mean()
                median_score = data2['Midterm'].median()
                percentile_category = calculate_percentile_category(midterm_score2, data2['Midterm'])

                st.write(f"Your Phonetics Midterm score is: {midterm_score2} out of 75 points ({(midterm_score2/75)*100:.1f}% accuracy)")
                st.write(f"Class Average (Mean): {mean_score:.2f}")
                st.write(f"Class Median: {median_score:.2f}")
                st.write(f"Your Performance Category: {percentile_category}")
            else:
                st.write("Invalid Passcode for Phonetics Midterm Score. Please try again.")
        
        if st.button("💫 Show Phonetics Score Dot Plot", key="tab2_dotplot_button"):
            st.header("Phonetics Score Dot Plot")
            display_dot_plot(data2)
        
        if st.button("👪 Show Phonetics Boxplot by Group", key="tab2_boxplot_button"):
            st.header("Phonetics Scores by Group")
            display_group_boxplot(data2)
