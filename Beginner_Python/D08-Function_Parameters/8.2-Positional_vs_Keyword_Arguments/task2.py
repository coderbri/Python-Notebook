# * Functions with 1 Input
def greet_by_name(name):
    print(f"Hello {name}!")

greet_by_name("Bri")


# * Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}.")

# * Positional Argument
greet_with("Jane Doe", "New York")

# * Keyword Argument
greet_with(location="Los Angeles", name="John Smith")
