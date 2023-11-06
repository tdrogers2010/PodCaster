
from pylib.ask_gpt3 import ask_gpt3

def main():
    input_message = "What is the weather like today?"
    assistant_reply, tokens_used = ask_gpt3(input_message)
    print("GPT-3.5 Assistant Reply:", assistant_reply)
    print("Tokens used for the reply:", tokens_used)

if __name__ == "__main__":
    main()
