print(10 % 5)  # output: 0
print(10 % 3)  # output: 1

number_to_check = int(input("What is the number you want to check? "))
print(f"Your number is: {number_to_check}.")

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")
