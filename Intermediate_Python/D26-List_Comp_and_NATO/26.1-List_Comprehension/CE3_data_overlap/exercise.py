with open("file1.txt", mode="r") as file:
    f1_contents = file.readlines()
    # print("F1", f1_contents)
    num_list1 = [int(num.strip()) for num in f1_contents]
    print(num_list1)    # [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]

with open("file2.txt", mode="r") as file:
    f2_contents = file.readlines()
    # print("F2", f2_contents)
    num_list2 = [int(num.strip()) for num in f2_contents]
    print(num_list2)    # [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]

result = [common_num for common_num in num_list1 if common_num in num_list2]
print(result)           # [3, 6, 5, 33, 12, 7, 42, 13]

"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
You are going to create a list called result which contains the numbers that are common in both files. 
e.g. if file1.txt contained: 
1 
2 
3
and file2.txt contained: 
2
3
4
result = [2, 3]

IMPORTANT:  The output should be a list of integers and not strings!
Try to use List Comprehension instead of a Loop.
"""