import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from wordcloud import WordCloud
import streamlit.components.v1 as components  # For embedding YouTube videos

# Function to create word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Streamlit tabs
tabs = st.tabs(["📈 QR", "⏳ Timer", "👥 Grouping", "⛅ Word Cloud"])

# QR Code tab
with tabs[0]:
    st.subheader("QR Code Generator")
    qr_link = st.text_input("Enter a link to generate a QR code:")

    # Adding a 'Generate QR Code' button
    generate_qr_button = st.button("Generate QR Code")
    
    if generate_qr_button and qr_link:
        # Generate the QR code only when the button is clicked
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_link)
        qr.make(fit=True)

        qr_img = qr.make_image(fill='black', back_color='white')

        # Convert the QR code image to RGB format and resize
        qr_img = qr_img.convert('RGB')  # Convert to RGB to be compatible with st.image
        qr_img = qr_img.resize((600, 600))  # Resize the image

        # Display the resized image using Streamlit
        st.image(qr_img, caption="Generated QR Code", use_column_width=False, width=400)

# Timer tab
with tabs[1]:
    # Embed the Hugging Face space as an iframe
    huggingface_space_url = "https://MK-316-mytimer.hf.space"
    
    # Use Streamlit components to embed the external page
    st.components.v1.html(f"""
        <iframe src="{huggingface_space_url}" width="100%" height="600px" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    """, height=600)

# Grouping tab
with tabs[2]:
    st.subheader("👥 Grouping Tool")

    # Upload file section
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    
    # User input for group size
    members_per_group = st.number_input("Members per Group", min_value=1, value=5)
    
    # Input for fixed groups (optional)
    fixed_groups_input = st.text_input("Fixed Groups (separated by semicolon;)", placeholder="Name1, Name2; Name3, Name4")

    # Submit button to trigger grouping process
    if st.button("Submit"):
        if uploaded_file is not None:
            # Function to group names
            def group_names(file, members_per_group, fixed_groups_input):
                # Read the CSV file
                df = pd.read_csv(file)

                # Parse fixed groups input
                fixed_groups = [group.strip() for group in fixed_groups_input.split(';') if group.strip()]
                fixed_groups_df_list = []
                remaining_df = df.copy()

                # Process fixed groups and create a list for additional members to be added
                for group in fixed_groups:
                    group_names = [name.strip() for name in group.split(',') if name.strip()]
                    # Find these names in the DataFrame
                    matched_rows = remaining_df[remaining_df['Names'].isin(group_names)]
                    fixed_groups_df_list.append(matched_rows)
                    # Remove these names from the pool of remaining names
                    remaining_df = remaining_df[~remaining_df['Names'].isin(group_names)]

                # Shuffle the remaining DataFrame
                remaining_df = remaining_df.sample(frac=1).reset_index(drop=True)
                
                # Adjusting fixed groups to include additional members if they're under the specified group size
                for i, group_df in enumerate(fixed_groups_df_list):
                    while len(group_df) < members_per_group and not remaining_df.empty:
                        group_df = pd.concat([group_df, remaining_df.iloc[[0]]])
                        remaining_df = remaining_df.iloc[1:].reset_index(drop=True)
                    fixed_groups_df_list[i] = group_df  # Update the group with added members

                # Grouping the remaining names
                groups = fixed_groups_df_list  # Start with adjusted fixed groups
                for i in range(0, len(remaining_df), members_per_group):
                    groups.append(remaining_df[i:i + members_per_group])

                # Determine the maximum group size
                max_group_size = max(len(group) for group in groups)
                
                # Creating a new DataFrame for grouped data with separate columns for each member
                grouped_data = {'Group': [f'Group {i+1}' for i in range(len(groups))]}
                # Add columns for each member
                for i in range(max_group_size):
                    grouped_data[f'Member{i+1}'] = [group['Names'].tolist()[i] if i < len(group) else "" for group in groups]

                grouped_df = pd.DataFrame(grouped_data)
                
                return grouped_df

            # Call the group_names function and display the grouped names
            grouped_df = group_names(uploaded_file, members_per_group, fixed_groups_input)
            
            # Display the grouped names
            st.write(grouped_df)
            
            # Option to download the grouped names as CSV
            csv = grouped_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Grouped Names as CSV",
                data=csv,
                file_name='grouped_names.csv',
                mime='text/csv',
            )

        else:
            st.error("Please upload a CSV file before submitting.")

# Word Cloud tab
with tabs[3]:
    st.subheader("🌌 Word Cloud Generator")

    # Input text for generating the word cloud
    user_input = st.text_area("Enter text to generate a word cloud:")

    # Button to generate the word cloud
    if st.button("Generate Word Cloud"):
        if user_input.strip():
            # Generate word cloud only when there is valid input
            wordcloud = create_wordcloud(user_input)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.warning("Please enter some text to generate a word cloud.")
