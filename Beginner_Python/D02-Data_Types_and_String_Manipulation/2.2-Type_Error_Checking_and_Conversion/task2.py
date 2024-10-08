# * Resolving TypeError
# len(12345)    # ! TypeError
len("Hello")    # 5

# Type Checking
print(type("Hello"))    # <class 'str'>
print(type(123))        # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>

# Type Conversion
print(int("123") + int("456"))  # 579

"""
Functions to Type Cast
str(), int(), float(), bool()
"""

name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) # <class 'str'>
print(type(length_of_name)) # <class 'int'>

print("Number of letters in your name: " + str(length_of_name))
# Numbers of letter in your name: 8