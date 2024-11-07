import streamlit as st
from deep_translator import GoogleTranslator
from io import BytesIO
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
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
}

# Translation function using deep-translator
def translate_text(text, target_language):
    """
    Translates the given text into the target language.

    Parameters:
    - text (str): The text to translate.
    - target_language (str): The language code for the target language (e.g., 'de' for German, 'fr' for French).

    Returns:
    - str: The translated text.
    """
    # Use deep-translator's GoogleTranslator
    translator = GoogleTranslator(source='auto', target=target_language)
    translated_text = translator.translate(text)
    return translated_text

# Text-to-Speech function using ElevenLabs API
def generate_speech(text, voice="Brian", model="eleven_multilingual_v2"):
    audio_generator = client.generate(text=text, voice=voice, model=model, stream=True)
    audio_data = BytesIO()
    for chunk in audio_generator:
        audio_data.write(chunk)
    audio_data.seek(0)
    return audio_data

# Streamlit app
st.title("Text Translator with Speech")

# Input text
user_text = st.text_area("Enter text to translate and convert to speech:")

# Target language selection with supported language codes
target_language = st.selectbox("Select the language to translate to:", supported_languages.keys())
target_language_code = supported_languages[target_language]  # Get the corresponding language code

# Translate button
if st.button("Translate"):
    if user_text:
        # Perform translation
        translated_text = translate_text(user_text, target_language_code)
        
        # Display original and translated text
        st.markdown("### Original Text:")
        st.write(user_text)
        
        st.markdown("### Translated Text:")
        st.markdown(
            f"""
            <div style="
                padding: 10px;
                border-radius: 5px;
                background-color: #f0f2f6;
                font-size: 1.1em;
                color: #333333;
                border: 1px solid #ddd;
                ">
                {translated_text}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Text-to-Speech for the Original Text
        st.markdown("#### Listen to Original Text")
        audio_data_original = generate_speech(user_text, voice="Brian", model="eleven_multilingual_v2")
        st.audio(audio_data_original, format="audio/mpeg")
        st.download_button(
            label="Download Original Audio",
            data=audio_data_original,
            file_name="original_text_audio.mp3",
            mime="audio/mpeg"
        )

        # Text-to-Speech for the Translated Text
        st.markdown("#### Listen to Translated Text")
        audio_data_translated = generate_speech(translated_text, voice="Lily", model="eleven_multilingual_v2")
        st.audio(audio_data_translated, format="audio/mpeg")
        st.download_button(
            label="Download Translated Audio",
            data=audio_data_translated,
            file_name="translated_text_audio.mp3",
            mime="audio/mpeg"
        )

    else:
        st.warning("Please enter some text to translate.")