import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the ElevenLabs API endpoint for text-to-speech
api_version = "v1"
voiceid = "wTV3G9KHdaVU6P2ZidG7" #Taylor Hoping to Be
url = f"https://api.elevenlabs.io/{api_version}/text-to-speech/" + voiceid

# Get the ElevenLabs API Key from environment variables
api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    raise ValueError("Error: ELEVENLABS_API_KEY not found in environment variables.")

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": api_key
}

def generate_voiceover(text):
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    try:
        # Make the API call
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        # Write the audio content to a file if response is successful
        with open('output.mp3', 'wb') as f:
            f.write(response.content)
        return "Voiceover generated successfully."
    except requests.RequestException as e:
        # Handle any errors that occur during the API call
        raise ConnectionError(f"API request failed: {e}")

# Test the function
if __name__ == "__main__":
    input_text = "I'mm the best"
    result = generate_voiceover(input_text)
    print(result)
