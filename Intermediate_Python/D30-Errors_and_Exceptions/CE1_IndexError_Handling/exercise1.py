##############################################################
# Exercise:       IndexError Handling
# Description:    Practicing Exception Handling (Try-Except).
#                 Specifically catching IndexError to provide
#                 a default fallback value when a list index
#                 is out of range.
##############################################################
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        # Try to get the fruit and print the specific pie
        fruit = fruits[index]
        print(fruit + " pie")

    except IndexError:
        # If the index was wrong, print the default "Fruit pie"
        print("Fruit pie")


make_pie(4)

