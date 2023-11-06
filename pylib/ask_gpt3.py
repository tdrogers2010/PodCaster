import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the endpoint for GPT-3.5 chat model with configurable version
api_version = "v1"
url = f"https://api.openai.com/{api_version}/chat/completions"

# Get the OpenAI API Key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Error: OPENAI_API_KEY not found in environment variables.")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def ask_gpt3(input_message):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": input_message}
    ]

    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }

    try:
        # Make the API call using the json parameter instead of data
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        response_json = response.json()

        # Extract the generated text and usage details
        if 'choices' in response_json and 'usage' in response_json:
            assistant_reply = response_json['choices'][0]['message']['content']
            tokens_used = response_json['usage']['total_tokens']
            return assistant_reply, tokens_used
        else:
            error_message = response_json.get('error', {}).get('message', "Unexpected API response")
            raise ValueError(f"API error: {error_message}")
    except requests.RequestException as e:
        raise ConnectionError(f"Network error: {e}")

# Test the function
if __name__ == "__main__":
    user_message = "List 5 most interesting questions to ask."
    reply, tokens = ask_gpt3(user_message)
    print(f"Reply: {reply}\nTokens used: {tokens}")
