import streamlit as st
from io import BytesIO
from deep_translator import GoogleTranslator
from elevenlabs import ElevenLabs
from pydub import AudioSegment
import config

# Set up ElevenLabs API
client = ElevenLabs(api_key=config.YOUR_API_KEY)

# Set ffmpeg and ffprobe paths if needed (Update these paths accordingly)
AudioSegment.ffmpeg = "/path/to/ffmpeg"
AudioSegment.ffprobe = "/path/to/ffprobe"

# Supported languages for translation
supported_languages = {
    "English": "en",
    "German": "de",
    "French": "fr",
    "Spanish": "es",
    "Italian": "it",
}

# Supported voices for ElevenLabs
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
        
        # Generate audio for each part of the conversation
        audio1 = generate_speech(text1_translated, voice=voice1)
        audio2 = generate_speech(text2_translated, voice=voice2)

        # Combine audio files using pydub
        audio1_segment = AudioSegment.from_file(audio1, format="mp3")
        audio2_segment = AudioSegment.from_file(audio2, format="mp3")
        combined_audio = audio1_segment + audio2_segment

        # Export the combined audio to BytesIO
        combined_audio_data = BytesIO()
        combined_audio.export(combined_audio_data, format="mp3")
        combined_audio_data.seek(0)

        # Play the combined audio
        st.markdown("#### Conversation Audio")
        st.audio(combined_audio_data, format="audio/mpeg")

        # Download combined audio
        st.download_button(
            label="Download Combined Conversation Audio",
            data=combined_audio_data,
            file_name="conversation_audio.mp3",
            mime="audio/mpeg"
        )
    else:
        st.warning("Please enter text for both Person 1 and Person 2.")