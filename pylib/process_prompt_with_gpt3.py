import os
from ask_gpt3 import ask_gpt3

def save_content_to_file(content, output_path):
    """
    Ensures the output directory exists and then saves the provided content to an output file.

    Parameters:
    - content: The content to be saved.
    - output_path: The path to the text file where the content will be saved.
    """
    # Extract the directory from the output path
    directory = os.path.dirname(output_path)
    
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the content to the file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def create_and_save_podcast(prompt, base_directory, segment_name, corpus_name="Corpus"):
    """
    Creates a podcast script based on the given prompt using GPT-3 and saves it to the specified directory.

    Parameters:
    - prompt: The prompt string to generate the podcast script.
    - base_directory: The root directory for storing the generated content.
    - segment_name: The specific category or segment name for the content within the corpus.
    - corpus_name: The directory name for the collection of related content. Defaults to 'Corpus'.
    """
    # Extend the prompt with a request for supporting materials
    ResourcesNeeded = (
        prompt +
        "\nDetermine what supporting materials would help you generate this podcast and you are capable "
        "of generating. Top 3."
    )
    
    # Determine what is needed (First GPT-3 Interaction)
    messages_to_send1 = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": ResourcesNeeded}
    ]
    assistant_reply1, tokens_used1 = ask_gpt3(messages_to_send1)
    output_path1 = os.path.join(base_directory, corpus_name, segment_name, "ResourcesToGenerate.txt")
    save_content_to_file(assistant_reply1, output_path1)

    # Create a table with the resources needed (Second GPT-3 Interaction)
    messages_to_send2 = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": assistant_reply1},
        {"role": "user", "content": "Create a table with Columns SupportingMaterialName, SupportingMaterialText"}
    ]
    assistant_reply2, tokens_used2 = ask_gpt3(messages_to_send2)
    output_path2 = os.path.join(base_directory, corpus_name, segment_name, "ResourcesToGenerateTable.txt")
    save_content_to_file(assistant_reply2, output_path2)

if __name__ == "__main__":
    print("Script started...")

    # Define the script's directory and base directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)  # Navigate up one directory from the script's location

    # Define the segment name for the output content
    segment_name = "PavementDiscussion"

    # Define the prompt for the GPT-3 generated podcast script
    podcast_prompt = (
        "We are going to write the script for a fictional podcast between Donald Trump and Joe Rogan "
        "about concrete vs asphalt pavement. The podcast should sound natural and engaging."
    )

    # Call the function to create and save the podcast with the provided prompt
    create_and_save_podcast(podcast_prompt, base_dir, segment_name)

    print("Process complete.")
