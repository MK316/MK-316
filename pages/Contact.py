import streamlit as st

st.header(":mailbox: Get in touch with me!")

contact_form = """
<form action="https://formsubmit.co/mirankim316@gmail.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
