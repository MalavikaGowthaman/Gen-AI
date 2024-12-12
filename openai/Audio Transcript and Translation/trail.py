import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPEN_API_KEY

audio_file = open("tamil_dialogue.mp3","rb")
output = openai.Audio.translate("whisper-1",audio_file)
print(output)