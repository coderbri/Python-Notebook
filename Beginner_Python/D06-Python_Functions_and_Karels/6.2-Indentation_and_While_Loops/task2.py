"""Indentation Notes
def my_function():
    print("Hello")      # Within a function
    print("World")      # Within a function

print("Hello World")    # Independent of function
"""

sky = "cloudy"

def how_are_you():
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
    print("World")

print("Hello")
how_are_you()
# Hello grey World
