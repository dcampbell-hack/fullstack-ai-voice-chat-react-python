import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven Labs
# Convert Text to Speech
def convert_text_to_speech(message):
    body = {
        "text": message,
        "voice_setting": {
            "stability": 0,
            "similarity_boost": 0,
        }
    }
    # Define voice
    voice_naomi = "21m00Tcm4TlvDq8ikWAM"

    # Constructing Headers and Endpoint
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_naomi}"

    # Send request
    try:
      response = requests.post(endpoint, json=body, headers=headers )
    except Exception as e:
        return
    
    # Handle Response
    if response.status_code == 200:
       return response.content
    else:
       return



