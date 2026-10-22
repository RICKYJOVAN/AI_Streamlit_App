import streamlit as st

st.set_page_config(
    page_title="AI-enabled Web Application",
    page_icon="🤖",
    layout="centered",
)

st.title("AI-enabled Web Application")
st.write("Welcome to the AI-enabled Web Application deployed using Streamlit Community Cloud.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name.strip():
        st.success(f"Hello, {name}! Your application is running successfully.")
    else:
        st.warning("Please enter your name first!")
