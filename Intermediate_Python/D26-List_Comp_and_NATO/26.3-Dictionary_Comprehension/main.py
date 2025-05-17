import random

names = ["Alex", "Britt", "Caroline", "Dave", "Eleanor", "Frederich"]

#  Create a dictionary where keys are student names and values are random scores (1-100)
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)  # Example: {'Alex': 39, 'Britt': 87, 'Caroline': 47, 'Dave': 74, 'Eleanor': 91, 'Frederich': 64}

# Create a new dictionary containing only students with passing scores (score > 60)
passed_students = {student: score for student, score in student_scores.items() if score > 60}
print(passed_students)  # Example: {'Britt': 87, 'Dave': 74, 'Eleanor': 91, 'Frederich': 64}