import json
import difflib  # For suggesting similar words
from difflib import get_close_matches

# Step 1: Load the JSON data into a dictionary
# Assuming the data.json file is in the same folder
def load_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

# Step 2: Create a function to get the definition of the word
def get_definition(word, dictionary):
    word = word.lower()  # Convert the word to lowercase to ensure case insensitivity

    # Step 3: Check if the word is in the dictionary
    if word in dictionary:
        return dictionary[word]

    # Step 4: Check for close matches using difflib
    close_matches = get_close_matches(word, dictionary.keys(), n=3, cutoff=0.8)
    if close_matches:
        suggestion = close_matches[0]  # Take the closest match
        user_response = input(f"Did you mean '{suggestion}' instead? (y/n): ")
        if user_response.lower() == 'y':
            return dictionary[suggestion]
        else:
            return "Word not found in the dictionary."
    else:
        return "Word not found in the dictionary and no close matches."

# Step 5: Prompt user input and search for definition
def main():
    dictionary_data = load_data("data.json")  # Replace 'data.json' with your file path
    while True:
        word = input("Enter a word to search for its definition (or 'q' to quit): ")
        if word.lower() == 'q':
            print("Exiting the dictionary.")
            break
        
        definition = get_definition(word, dictionary_data)
        
        if isinstance(definition, list):  # If multiple definitions exist
            for idx, def_item in enumerate(definition, 1):
                print(f"Definition {idx}: {def_item}")
        else:
            print(definition)

if __name__ == "__main__":
    main()
