# Variable 1
name = "Bri"
length = len(name)
print("Name is: " + name + " - " + str(length))

# Variable 2
username = "coderBri"
other_length = len(username)
print("Username is: " + username + " - " + str(other_length))

# Variable Reassignment
temp = name
name = username
username = temp

print("\n")
print("Name is now: " + name + " - " + str(length))
print("Username is now: " + username + " - " + str(length))
