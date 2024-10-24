import streamlit as st
from .users import users, check_password

def authenticate(username, password):
    if username in users:
        return check_password(password, users[username])
    return False

def login_form():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True  # Set the login flag
            st.success("Login successful!")
        else:
            st.error("Login failed. Please try again.")
