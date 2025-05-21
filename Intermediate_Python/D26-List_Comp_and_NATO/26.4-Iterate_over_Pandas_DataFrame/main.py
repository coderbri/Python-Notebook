student_dict = {
    "student": ["Ava", "Bethany", "Catherine"],
    "score": [56, 76, 98]
}

# ? See txt file for solutions

# * Looping through dictionaries
# for (key, value) in student_dict.items():
    #         Key => Value
    # print(f"{key} => {value}")

import pandas

student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)
#      student  score
# 0        Ava     56
# 1    Bethany     76
# 2  Catherine     98

# * Looping through a DataFrame
# for (key, value) in student_dataframe.items():
    # print(key)
    # print(value)

# * Looping through rows of a dataframe
for (index, row) in student_dataframe.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Ava":
        print(f"Ava's score: {row.score}")
    else:
        print("- Access denied -")
