# * Read-Only
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# * Write New Text
# with open("my_file.txt", mode="w") as file:
#     file.write("你好，我是coderBri。\n我是一名来自美国的软件开发人员。")


# * Add New Text
with open("my_file.txt", mode="a") as file:
    file.write("\n你好，我是coderBri。\n我是一名来自美国的软件开发人员。")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# * Creating a File for New Text
with open("new_file.txt", mode="w") as file:
    file.write("New text is here...")

with open("new_file.txt") as file:
    contents = file.read()
    print(contents)
