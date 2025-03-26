import os

PLACEHOLDER = "[name]"

# ? Get the absolute path of the script's directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# ? Define paths using os.path.join()
input_names_path = os.path.join(base_dir, "Input/Names/invited_names.txt")
input_letter_path = os.path.join(base_dir, "Input/Letters/starting_letter.txt")
output_dir = os.path.join(base_dir, "Output/ReadyToSend")

os.makedirs(output_dir, exist_ok=True)  # ? Ensure directory exists


# TODO: Create a letter using starting_letter.txt
# * 1. For each name in invited_names.txt, replace the [name] placeholder with the actual name.

with open(input_names_path, mode="r") as names_file:
    list_of_names = names_file.readlines()
    # print(list_of_names)
    # Output: ['Aang\n', 'Zuko\n', ..., 'Toph']

with open(input_letter_path, mode="r") as letter_file:
    letter_contents = letter_file.read()
    for name in list_of_names:
        formatted_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, formatted_name)
        # print(new_letter)

        # * 2. Save the letters in the folder "ReadyToSend".
        letter_output_path = os.path.join(output_dir, f"letter_for_{formatted_name}.txt")
        with open(letter_output_path, mode="w") as completed_letter:
            completed_letter.write(new_letter)

print("Mail merge complete! Check the 'ReadyToSend' folder.")

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp