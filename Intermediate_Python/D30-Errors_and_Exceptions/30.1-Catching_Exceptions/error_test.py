##############################################################
# Exercise:       ValueError Handling
# Description:    Example of raising custom exceptions. 
#                 Demonstrates how to manually trigger a 
#                 ValueError to enforce business logic (e.g., 
#                 preventing unrealistic physical inputs).
##############################################################

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    # Manually triggering an error because the input is logically "wrong"
    # even if the math would technically work.
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(f"Your BMI is: {bmi}")