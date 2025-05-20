sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words = sentence.split()
# ['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']

num_of_letters_per_word = [len(letter) for letter in words]
# [4, 2, 3, 8, 8, 2, 2, 7, 8]

result = {word: len(word) for letter in words for word in words}
print(result)
# {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

"""
You are going to use Dictionary Comprehension to create a dictionary called result that 
takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.  *
*Do NOT** Create a dictionary directly.
Try to use Dictionary Comprehension instead of a Loop.

To keep this exercise simple, count any punctuation following a word with no whitespace 
as part of the word. Note that "Swallow?" therefore has a length of 8.
"""