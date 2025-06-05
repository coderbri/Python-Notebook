# The 'calculate' function takes a positional argument 'n'
# and then accepts any number of additional keyword arguments via '**kwargs'.
def calculate(n, **kwargs):
    # '**kwargs' collects all unexpected keyword arguments into a dictionary.
    # We can inspect its type to confirm it's a dictionary.
    print(f"Type of kwargs: {type(kwargs)}")
    # Print the dictionary to see its contents.
    print(f"Contents of kwargs: {kwargs}")

    # You can iterate over the items (key-value pairs) in the kwargs dictionary.
    print("\nIterating through kwargs:")
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")

    # You can access specific values from the kwargs dictionary using their keys,
    # just like with any other dictionary.
    print(f"\nValue for 'add' key: {kwargs['add']}")

    # Use the values from kwargs to perform calculations.
    n += kwargs['add']      # Add the value associated with the 'add' key to 'n'.
    n *= kwargs['multiply'] # Multiply 'n' by the value associated with the 'multiply' key.
    print(f"Calculated result: {n}")

# When calling 'calculate', 'n' gets '2', and 'add=3' and 'multiply=5'
# are collected into the 'kwargs' dictionary.
calculate(2, add=3, multiply=5)

# Expected Output:
# Type of kwargs: <class 'dict'>
# Contents of kwargs: {'add': 3, 'multiply': 5}
#
# Iterating through kwargs:
# Key: add, Value: 3
# Key: multiply, Value: 5
#
# Value for 'add' key: 3
# Calculated result: 25 (Calculation: (2 + 3) * 5)