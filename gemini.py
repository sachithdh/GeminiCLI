import google.generativeai as genai
import os
import argparse
import PIL.Image
import re
from dotenv import load_dotenv
# import textwrap

load_dotenv('/usr/gemini/config/.env')


# Fetch API key from environment variable
GOOGLE_API_KEY = os.getenv('API_KEY')

# Configure the generative AI library with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-pro-latest')


# Parse command line arguments
def arg_parse():
    """
    Parses command line arguments to extract the prompt.

    Returns:
        str: The prompt extracted from command line arguments.
    """
    parser = argparse.ArgumentParser(description='Gemini AI for terminal')

    parser.add_argument('-i', '--img', type=str, help='Path to an image')

    parser.add_argument('words', nargs='*', type=str, help='The words to print')

    # Parse the command-line arguments
    args = parser.parse_args()


    if args.img:
        if args.words:
            phrase = ' '.join(args.words)
            img = PIL.Image.open(args.img)
            prompt = [phrase, img]

            return prompt
        else: 
            return "No valid prompt provided."

    # Join the words into a single phrase if no other options are provided
    if args.words:
        phrase = ' '.join(args.words)
        return phrase

    # Default message if no valid arguments are provided
    return "No valid arguments provided."


def get_response(prompt):
    response = model.generate_content(
        prompt,
        generation_config = genai.types.GenerationConfig(
            candidate_count = 1,
            temperature = 0.5
        )
        stream=True
    )
    for chunk in response:
        to_display(chunk.text)


# Format text for display
def to_display(text):
    """
    Formats the generated text for display.

    Args:
        text (str): The generated text to be formatted.

    Returns:
        str: The formatted text ready for display.
    """
    text = text.replace('**', '')
    text = text.replace('*', '\n    •')

    text = text.replace("##", "")
    text = re.sub(r'\*\*(.*?)\*\*', r'\033[1m\1\033[0m', text, flags=re.DOTALL)
    text = re.sub(r'\*(.*?)\*', r'\033[3m\1\033[0m', text, flags=re.DOTALL)
    text = re.sub(r'^(    \*.*)$', r'\n\1', text, flags=re.MULTILINE)

    print(text)
    

def main():
    """
    Main function to execute the program.
    """
    prompt = arg_parse()
    get_response(prompt)

if __name__ == "__main__":
    main()

