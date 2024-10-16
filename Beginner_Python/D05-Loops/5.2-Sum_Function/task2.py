student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

# * Sum Function
total_exam_score = sum(student_scores)
print(total_exam_score)     # 2068

# Sum via For Loop
sum_of_scores = 0
for score in student_scores:
    sum_of_scores += score
print("Sum of Student Scores: " + str(sum_of_scores))
# Sum of Student Scores: 2068

# * Max Function
max_score = max(student_scores)
print(max_score)            # 199

# Max via For Loop
max_score2 = 0
for score in student_scores:
    if score > max_score2:
        max_score2 = score

print("Max Score: " + str(max_score2))
# Max Score: 199

# * Min Function
min_score = min(student_scores)
print(min_score)

# Min via For Loop
min_score2 = student_scores[0]  # 150
for score in student_scores:
    if score < min_score2:
        min_score2 = score

print("Min Score: " + str(min_score2))
# Min Score: 24
