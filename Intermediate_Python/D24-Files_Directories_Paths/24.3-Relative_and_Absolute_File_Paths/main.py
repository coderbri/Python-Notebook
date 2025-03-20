# * Creating a File for New Text
# ! Replace the user with your own username to see this work:
# ! This written for Mac, use C: to access the root directory for absolute file paths
with open("/Users/[your_username]/Desktop/test.txt", mode="w") as file:
    file.write("Using file path to create this file and write some text")

with open("/Users/[your_username]/Desktop/test.txt") as file:
    contents = file.read()
    print(contents)


# * Creating a File using Relative File Paths
with open("/Users/[your_username]/Desktop/test.txt", mode="w") as file:
    file.write("Using relative file paths to create read what I have written in this file")

with open("../../../../Desktop/test.txt") as file:
    contents = file.read()
    print(contents)