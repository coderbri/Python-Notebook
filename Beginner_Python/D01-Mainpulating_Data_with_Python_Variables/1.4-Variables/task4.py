print("=== VERSION 1 ===")
name = input("What is your name? ")
print("Hello " + name + "!")

print("\nThe length of this name is: ")
print(len(name))


print("\n=== VERSION 2 ===")
print(len(input("What is your name? "))) # Bri\n3

# Most Efficient
print("\n=== VERSION 23 ===")
username = input("Hello user! What is your username? ")
length = len(username)
print("Hello " + username + "! Your username is " + str(length) + " characters long.")