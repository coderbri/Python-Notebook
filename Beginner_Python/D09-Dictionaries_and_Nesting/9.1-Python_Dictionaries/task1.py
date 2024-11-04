programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# * Accessing items in a dictionary
print(programming_dictionary["Function"])
# Output: A piece of code that you can easily call over and over again.

# * Adding key:values
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)   # Prints the whole dictionary, as defined at the top.

# * Initializing a Dictionary
empty_dictionary = {}
empty_dictionary["first entry"] = "Hello World"
print(empty_dictionary)         # {'first entry': 'Hello World'}

# * Wipe an Existing Dictionary
# programming_dictionary = {}
# print(programming_dictionary)   # {}

# * Edit an Item in a Dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)
# Output: {'Bug': 'A moth in your computer.',... }

# * Loop Through a Dictionary
for vocab in programming_dictionary:
    print(vocab)                          # Prints Key
    print(programming_dictionary[vocab])  # Prints Value
# Output (In respective line): Bug Function Loop
