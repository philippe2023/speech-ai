# VoiceVerse

VoiceVerse is a versatile application built with Streamlit, allowing users to experience advanced text-to-speech, translation, and conversational simulations. This app leverages the ElevenLabs API for high-quality voice synthesis and `deep-translator` for translation capabilities.

## Features

- **Text-to-Speech**: Enter text and listen to it spoken in different voices and languages.
- **Translation**: Translate text between supported languages.
- **Translate & Speak**: Translate text and generate audio in the translated language.
- **Simulated Conversation**: Create a back-and-forth conversation between two people with different text inputs, voices, and languages.
- **Merged Conversation Audio**: Simulate a conversation and merge both audio clips into a single file.

## Project Structure

The application is organized as follows:

```
app/
├── main.py                 # Main app file with sidebar navigation
├── pages/
│   ├── speech.py           # Page for basic text-to-speech
│   ├── translator.py       # Page for translation
│   ├── translator_plus.py  # Page for translation + TTS
│   ├── convo.py            # Page for basic conversation simulation
│   └── convo_merge.py      # Page for merged conversation audio
└── config.py               # File for API keys and configuration
```

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd voiceverse
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have `ffmpeg` installed on your system, as it is required by `pydub`:

   - **macOS**: `brew install ffmpeg`
   - **Ubuntu**: `sudo apt-get install ffmpeg`
   - **Windows**: Download and add to system PATH from [ffmpeg.org](https://ffmpeg.org/download.html).

4. Set up API keys:

   - In `config.py`, add your ElevenLabs API key.

## Usage

To start the app, run:

```bash
streamlit run app/main.py
```

Then, use the sidebar to navigate through the different features.

## Requirements

- Streamlit
- ElevenLabs Python API
- deep-translator
- pydub
- ffmpeg (for audio processing)

## License

This project is licensed under the MIT License.
