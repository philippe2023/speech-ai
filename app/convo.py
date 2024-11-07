import streamlit as st
from io import BytesIO
from deep_translator import GoogleTranslator
from elevenlabs import ElevenLabs
import config

# Set up ElevenLabs API
client = ElevenLabs(api_key=config.YOUR_API_KEY)

# Supported languages for translation
supported_languages = {
    "English": "en",
    "German": "de",
    "French": "fr",
    "Spanish": "es",
    "Italian": "it",
}

# Supported voices for ElevenLabs (add more voices as needed)
voices = ["Brian", "Lily"]

# Translation function
def translate_text(text, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)
    return translator.translate(text)

# Text-to-Speech function
def generate_speech(text, voice="Brian", model="eleven_multilingual_v2"):
    audio_generator = client.generate(text=text, voice=voice, model=model, stream=True)
    audio_data = BytesIO()
    for chunk in audio_generator:
        audio_data.write(chunk)
    audio_data.seek(0)
    return audio_data

# Streamlit app for conversation
st.title("Simulated Conversation")

# Input for Person 1
st.markdown("### Person 1")
text1 = st.text_area("Enter text for Person 1:")
language1 = st.selectbox("Select Person 1's language:", supported_languages.keys())
voice1 = st.selectbox("Select Person 1's voice:", voices)

# Input for Person 2
st.markdown("### Person 2")
text2 = st.text_area("Enter text for Person 2:")
language2 = st.selectbox("Select Person 2's language:", supported_languages.keys())
voice2 = st.selectbox("Select Person 2's voice:", voices)

# Generate button
if st.button("Generate Conversation"):
    if text1 and text2:
        # Translate text if necessary
        text1_translated = translate_text(text1, supported_languages[language1])
        text2_translated = translate_text(text2, supported_languages[language2])
        
        # Combine text as a conversation
        combined_text = f"Person 1 says: {text1_translated}. Person 2 responds: {text2_translated}"

        # Generate audio for each part of the conversation
        audio1 = generate_speech(text1_translated, voice=voice1)
        audio2 = generate_speech(text2_translated, voice=voice2)

        # Play each person's audio in sequence
        st.markdown("#### Conversation Audio")
        st.audio(audio1, format="audio/mpeg")
        st.audio(audio2, format="audio/mpeg")

        # Create a combined audio download (optional)
        combined_audio = BytesIO()
        combined_audio.write(audio1.getbuffer())
        combined_audio.write(audio2.getbuffer())
        combined_audio.seek(0)

        st.download_button(
            label="Download Combined Conversation Audio",
            data=combined_audio,
            file_name="conversation_audio.mp3",
            mime="audio/mpeg"
        )
    else:
        st.warning("Please enter text for both Person 1 and Person 2.")