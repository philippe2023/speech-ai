import streamlit as st
from deep_translator import GoogleTranslator

# Supported languages and their codes (all lowercase)
supported_languages = {
    "english": "en",
    "german": "de",
    "french": "fr",
    "spanish": "es",
    "italian": "it",
    "portuguese": "pt",
    "russian": "ru",
    "chinese (simplified)": "zh-CN",
    "japanese": "ja",
}

def translate_text(text, target_language):
    """
    Translates the given text into the target language.

    Parameters:
    - text (str): The text to translate.
    - target_language (str): The language code for the target language.

    Returns:
    - str: The translated text.
    """
    translator = GoogleTranslator(source='auto', target=target_language)
    translated_text = translator.translate(text)
    return translated_text

# Streamlit app
st.title("Text Translator")

# Input text
user_text = st.text_area("Enter text to translate:")

# Language selection using the exact lowercase language names
target_language = st.selectbox("Select the language to translate to:", list(supported_languages.keys()))

# Map selected language name to the exact code
target_language_code = supported_languages[target_language.lower()]

# Translate button
if st.button("Translate"):
    if user_text:
        # Perform translation
        translated_text = translate_text(user_text, target_language_code)
        
        # Display translated text with styling
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
    else:
        st.warning("Please enter some text to translate.")