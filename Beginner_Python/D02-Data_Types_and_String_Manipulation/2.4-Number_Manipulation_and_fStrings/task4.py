weight = 84
height = 1.65
bmi = weight / height ** 2

print(bmi)              # 30.85399449035813
print(int(bmi))         # 30

print(round(bmi))       # 31

print(round(bmi, 2))    # 30.85

# * Assignment Operators
score = 0
score += 1
print(score)    # Output: 1

# * Using F-Strings
# print("Your score is " + score)       # ! TypeError - cannot combine strings and int values

print("Your score is " + str(score))    # Output: Your score is 1
print(f"Your score = {score}")          # Output: Your score = 1
print(f"Your weight is {weight}, and your height is {height}.\n > So your bmi is {bmi}.")
