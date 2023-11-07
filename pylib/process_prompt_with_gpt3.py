import os
from ask_gpt3 import ask_gpt3

def process_prompt_with_gpt3(prompt, output_path):
    """
    Processes a given prompt string using GPT-3 and saves the response to an output file.

    Parameters:
    - prompt: The prompt string for GPT-3.
    - output_path: The path to the text file where the GPT-3 response will be saved.
    """

    # Get the GPT-3.5 response
    assistant_reply, tokens_used = ask_gpt3(prompt)

    # Write the response to the output file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(assistant_reply)

if __name__ == "__main__":
    print("Script started...")

    # Use the script's directory to define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)  # This goes one directory up from the script's location
    
    # Define the prompt and output
    prompt1 = """
Lets build fictional characters Donald Tup (Parody of Donald trump) and Joe Ryan (Parody of Joe Rogan).  The Topic will be gravel types for road construction. 

Create a profile for each of these Fictional character.  Include PARODY OF: Parody of Name. Consider what each character cares about in this Topic.   Categorize the characters main speech attributes.  
"""
    filename1 = "characters.txt"


    # Specify the output file within the Corpus folder 
    directory_name = "Gravel"
    output_path = os.path.join(base_dir, "Corpus", directory_name, filename1)
    process_prompt_with_gpt3(prompt1, output_path)

    print(f"Processing complete. Output saved to {output_path}")
