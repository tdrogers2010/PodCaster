import requests

voiceid = "21m00Tcm4TlvDq8ikWAM"
url = "https://api.elevenlabs.io/v1/text-to-speech/" & voiceid

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "51577e00ba74e6b20632c70b407d83f8"
}

data = {
    "text": "Whhhatttsssuppp!",
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

response = requests.post(url, json=data, headers=headers)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Write the content in binary mode to a file
    with open('output.mp3', 'wb') as f:
        f.write(response.content)
else:
    print(f"Failed to generate speech. Status code: {response.status_code}")
    print(f"Response: {response.text}")
