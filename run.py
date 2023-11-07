import os
from pylib.ask_gpt3 import ask_gpt3

def main():
    # Specify the directory name within the Corpus folder
    directory_name = "Gravel"
    
    # Construct the paths to the prompt and output files
    base_path = os.path.join("Corpus", directory_name)
    prompt_path = os.path.join(base_path, "prompt.txt")
    output_path = os.path.join(base_path, "output.txt")

    # Read the prompt from the file
    with open(prompt_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    # Get the GPT-3.5 response
    assistant_reply, tokens_used = ask_gpt3(prompt)

    # Write the response to the output file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(assistant_reply)

if __name__ == "__main__":
    main()
