# Using the error the input prompts if users respond with
#   a string instead, make the exception catch that type of error.
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print("Sorry, kid. You're not old enough to drive.")
