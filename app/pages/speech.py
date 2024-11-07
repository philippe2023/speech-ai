import streamlit as st
from elevenlabs import ElevenLabs
import config
from io import BytesIO

# Set up ElevenLabs API
client = ElevenLabs(api_key=config.YOUR_API_KEY)

def text_to_speech_page():
    st.title("Text-to-Speech")

    # User input
    user_text = st.text_area("Enter text to convert to speech:")
    voice_choice = st.selectbox("Choose a voice", ["Brian", "George", "Lily", "Adam"])

    # Language selection for multilingual support
    language_choice = st.selectbox("Choose a language", ["English", "German", "French", "Spanish", "Italian"])
    
    # Map the language to a sample greeting text
    language_texts = {
        "English": "Hello!",
        "German": "Hallo!",
        "French": "Bonjour!",
        "Spanish": "¡Hola!",
        "Italian": "Ciao!"
    }
    
    # Combine the user's text with the language-specific greeting to help with language detection
    combined_text = language_texts[language_choice] + " " + user_text

    if st.button("Generate Speech"):
        if user_text:
            # Generate audio with streaming enabled and set the model to `eleven_multilingual_v2`
            audio_generator = client.generate(text=combined_text, voice=voice_choice, model="eleven_multilingual_v2", stream=True)
            
            # Collect all chunks into a BytesIO object
            audio_data = BytesIO()
            for chunk in audio_generator:
                audio_data.write(chunk)
            audio_data.seek(0)  # Reset to the beginning of the BytesIO buffer

            # Play in Streamlit
            st.audio(audio_data, format="audio/mpeg")

            # Create a download button
            st.download_button(
                label="Download Audio",
                data=audio_data,
                file_name="speech_output.mp3",
                mime="audio/mpeg"
            )
        else:
            st.warning("Please enter some text.")

# Display the page
if __name__ == "__main__":
    text_to_speech_page()