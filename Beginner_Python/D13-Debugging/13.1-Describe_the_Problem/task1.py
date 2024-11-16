def my_function():
    # Change this: for i in range(1, 20):
    for i in range(1, 21):
        if i == 20:
            print("You got it:)")

my_function()

# Describe the Problem - Write your answers as comments:
# * 1. What is the for loop doing?
# ? The variable `i` is iterating through a range from 1 to 19 (inclusive), but it never reaches 20.

# * 2. When is the function meant to print "You got it"?
# ? The function is intended to print "You got it" when `i` is equal to 20. However, because the range is set from 1 to 19, `i` never reaches 20, so the if-condition is never true.

# * 3. What are your assumptions about the value of i?
# ? The current range stops at 19, meaning `i` can only go as high as 19. To allow `i` to reach 20, we should extend the range to `range(1, 21)` to include 20.
