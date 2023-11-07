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

def ask_gpt3(messages):
    """
    Sends a list of messages to the OpenAI GPT-3.5 chat model and retrieves the response.

    Args:
        messages (list): The list of messages including system and user messages to send to the GPT-3.5 model.

    Returns:
        tuple:
            - assistant_reply (str): The model's response to the input message.
            - tokens_used (int): The number of tokens used in the API response.
    """
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
    system_message = "You are a helpful assistant."
    user_message = "List 5 most interesting questions to ask."
    messages_to_send = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    reply, tokens = ask_gpt3(messages_to_send)
    print(f"Reply: {reply}\nTokens used: {tokens}")
