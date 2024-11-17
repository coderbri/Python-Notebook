def fizz_buzz(target):
    for number in range(1, target + 1):
        # Check divisibility by both 3 and 5 first.
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # Check divisibility by 3 only.
        elif number % 3 == 0:
            print("Fizz")
        # Check divisibility by 5 only.
        elif number % 5 == 0:
            print("Buzz")
        else:
            # Print the number if no other condition is met.
            print(number)

# Prompt user for input and run FizzBuzz.
fizz_buzz(target=int(input("Enter Number: ")))
