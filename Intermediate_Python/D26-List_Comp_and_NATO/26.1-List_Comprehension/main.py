# * List Comprehension Practice
numbers = [ 1, 2, 3]
new_numbers = [n +1 for n in numbers]
print(new_numbers)      # [2, 3, 4]

name = "coderBri"
letters_list = [letter for letter in name]
print(letters_list)     # ['c', 'o', 'd', 'e', 'r', 'B', 'r', 'i']

new_list = [n*2 for n in range(1,5)]
print(new_list)         # [2, 4, 6, 8]

# * Conditional List Comprehension
names = ["Alex", "Brit", "Caroline", "Dave", "Eleanor", "Frederich"]
short_names = [name for name in names if len(name) < 6]
print(short_names)      # ["Alex", "Britt", "Dave"]

long_names = [n.upper() for n in names if len(n) > 5]
print(long_names)       # ['CAROLINE', 'ELEANOR', 'FREDERICH']
