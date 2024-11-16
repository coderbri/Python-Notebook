year = int(input("What's your year of birth?" ))

if year > 1980 and year < 1994:
    print("You are a millennial.")
# ! elif year > 1994: => Invalid Code
elif year >= 1994:
    print("You are a Gen Z.")

# The issue here is that the year 1994 is not taken into account, so nothing is printed.
# We can simulate as such below to debug the issue:
# year = 1994
# if year > 1980 and year < 1994:
# if True and False => This becomes a False and skips the print statement entirely.

# elif year > 1994:
# if False => this print statement has also been nulled so in the end, no lines of code will run.
# There needs to be at least one True if-clause to catch this value and print the answer.
