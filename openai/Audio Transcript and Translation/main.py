import openai
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Streamlit app setup
st.title("Audio Transcript and Translator")

# Instructions
st.write("Upload an audio file, choose a language, and get a transcript along with the translated output.")

# File upload widget
audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])
language = st.text_input("Enter the language for translation (e.g., Spanish, French)")

if audio_file and language:
    with st.spinner("Processing..."):
        # Save the uploaded file temporarily
        with open("temp_audio_file", "wb") as f:
            f.write(audio_file.read())

        # Open the file and perform transcription
        with open("temp_audio_file", "rb") as audio:
            transcript = openai.Audio.translate("whisper-1", audio)
        
        # Use the transcript text to get the translation
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"Translate the following text into {language}."},
                {"role": "user", "content": transcript["text"]}
            ],
            temperature=0,
            max_tokens=256
        )

        # Display the transcript and translation
        st.subheader("Transcript")
        st.write(transcript["text"])

        st.subheader("Translation")
        st.write(response['choices'][0]['message']['content'])

    # Clean up temporary audio file
    os.remove("temp_audio_file")
else:
    st.info("Please upload an audio file and specify a target language.")
