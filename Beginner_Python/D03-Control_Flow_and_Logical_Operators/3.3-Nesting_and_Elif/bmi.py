weight = 85
height = 1.85

bmi = weight / (height ** 2)
print(f"bmi: {round(bmi)}")

if bmi >= 25:
    print("You're overweight.")
elif bmi >= 18.5:
    print("You're normal weight.")
else:
    print("You're underweight.")