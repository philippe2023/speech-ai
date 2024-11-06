import streamlit as st
from elevenlabs import ElevenLabs
import app.config as config
from io import BytesIO

# Set up ElevenLabs API
client = ElevenLabs(api_key=config.YOUR_API_KEY)

def text_to_speech_page():
    st.title("Text-to-Speech")

    # User input
    user_text = st.text_area("Enter text to convert to speech:")
    voice_choice = st.selectbox("Choose a voice", ["Brian", "George", "Lily", "Adam"])

    if st.button("Generate Speech"):
        if user_text:
            # Generate audio with streaming enabled
            audio_generator = client.generate(text=user_text, voice=voice_choice, stream=True)
            
            # Collect all chunks into a BytesIO object
            audio_data = BytesIO()
            for chunk in audio_generator:
                audio_data.write(chunk)
            audio_data.seek(0)  # Reset to the beginning of the BytesIO buffer

            # Play in Streamlit
            st.audio(audio_data, format="audio/mpeg")
        else:
            st.warning("Please enter some text.")

# Display the page
if __name__ == "__main__":
    text_to_speech_page()
