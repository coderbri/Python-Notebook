student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

#  student
for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
