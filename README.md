# Meeting Minutes Generator

This repository contains a simple, barebone Flask web application that uses the OpenAI API to transcribe audio files and generate meeting minutes from the transcriptions. This app is intended for testing and educational purposes only and is not recommended for production use.

**Please note that calling the Whisper ASR API can be quite expensive. Be cautious and monitor your usage while testing this app.**

## Files

- `app.py`: The main Flask web application file.
- `ml_functions.py`: Contains helper functions for interacting with OpenAI's Whisper ASR and GPT-3.5 Turbo models.
- `requirements.txt`: Lists the required Python libraries for this project.

## Usage

1. Clone the repository.
2. Install the required Python libraries: `pip install -r requirements.txt`
3. Replace `'your_openai_api_key'` in `ml_functions.py` with your OpenAI API key (for testing purposes only, see disclaimer below).
4. Replace `'your_secret_key'` in `app.py` with a secure random string for Flask's secret key (for testing purposes only, see disclaimer below).
5. Run the Flask web application: `python app.py`
6. Access the web application at `http://localhost:5000/` or `http://127.0.0.1:5000/` and follow the on-screen instructions to upload an audio or video file and generate meeting minutes.

## Functionality

The Flask web application allows users to upload an audio or video file. The file is transcribed using OpenAI's Whisper ASR model, and the transcript is then processed by the GPT-3.5 Turbo model to generate meeting minutes, which are returned as a text file.

The generated meeting minutes include the following sections:

- Agenda
- Attendees
- Key Points
- Decisions
- Action Items

## Dependencies

- Flask: The web application framework.
- OpenAI: The Python library for interacting with the OpenAI API.

## Disclaimer

For the sake of simplicity, we're placing the OpenAI API key and Flask secret key directly in the code. However, in a production environment, it's recommended to store sensitive information like API keys and secret keys as environment variables. This app is for testing and educational purposes only. It is not designed for production use, and you should take necessary precautions to handle sensitive data, API keys, and other security concerns in a production environment.