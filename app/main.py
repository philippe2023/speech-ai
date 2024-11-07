import streamlit as st

# Page configurations
st.set_page_config(page_title="VoiceVerse", layout="wide")

st.title("Welcome to VoiceVerse")
st.write("""
    VoiceVerse is a versatile application that offers multiple language and voice-processing capabilities:
    
    - **Text-to-Speech**: Enter text and listen to it spoken in different voices and languages.
    - **Translation**: Translate text between supported languages.
    - **Translate & Speak**: Translate text and generate audio in the translated language.
    - **Simulated Conversation**: Create a back-and-forth conversation between two people with different text inputs, voices, and languages.
    - **Merged Conversation Audio**: Simulate a conversation and merge both audio clips into one file.
    
    Use the sidebar to navigate through the features.
    """)