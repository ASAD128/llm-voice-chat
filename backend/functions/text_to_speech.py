import os
import requests
from dotenv import load_dotenv

load_dotenv()
ELEVEN_LABS_API_KEY = os.environ.get("ELEVEN_LABS_API_KEY")

# Eleven Labs
# Convert text to speech
def convert_text_to_speech(message):
    payload = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }


    voice_rachel = "21m00Tcm4TlvDq8ikWAM"
    voice_antoni = "ErXwobaYiN019PkySvjV"

    # Construct request headers and url
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json",
        "accept": "audio/mpeg"
    }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

    try:
        response = requests.request("POST", endpoint, json=payload, headers=headers)
        print(response)
    except Exception as e:
        print("Oh nooo ")
        return

    if response.status_code == 200:
        # with open("output.wav", "wb") as f:
        #     f.write(audio_data)
        return response.content
    else:
        return
