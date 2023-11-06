import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the ElevenLabs API Key from environment variables
api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    raise ValueError("Error: ELEVENLABS_API_KEY not found in environment variables.")

def generate_voiceover(text, voice_id, similarity_boost=0.75, stability=0.5, style=0.92, use_speaker_boost=True):
    # Define the ElevenLabs API endpoint for text-to-speech with the voice ID
    api_version = "v1"
    url = f"https://api.elevenlabs.io/{api_version}/text-to-speech/{voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    # Initialize voice settings with default or provided values
    voice_settings = {
        "similarity_boost": similarity_boost,
        "stability": stability,
        "style": style,
        "use_speaker_boost": use_speaker_boost
    }

    # Data payload for post request
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": voice_settings
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
    input_text = "Hi! My name is Bella, nice to meet you!"
    voice_id = "21m00Tcm4TlvDq8ikWAM"  # Replace with your voice ID

    # Call the function with default settings
    result = generate_voiceover(input_text, voice_id)
    print(result)
