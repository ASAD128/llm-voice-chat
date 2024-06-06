import os
from functions.database import get_recent_messages
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

# Open AI - Whisper
# Convert audio to text
def convert_audio_to_text(audio_file):
    try:
        print("transcription from Whisper")
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        print(transcription)
        message_text = transcription.text
        return message_text
    except Exception as e:
        return

# Open AI - Chat GPT
# Convert audio to text
def get_chat_response(message_input):

    messages = get_recent_messages()
    user_message = { "role": "user", "content": message_input }
    messages.append(user_message)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print(response)
        message_text = response.choices[0].message.content
        return message_text
    except Exception as e:
        return
