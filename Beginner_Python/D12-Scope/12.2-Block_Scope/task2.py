# There is no Block Scope in Python!
# Unlike some other languages, Python does not have block scope. This means that
# variables created within if, for, or while statements are accessible outside of those blocks.

# ? Variable declared inside an if block, accessible outside due to lack of block scope
if 3 > 2:
    a_variable = 10  # Accessible outside this if block because Python has no block scope

# * Global variable (accessible anywhere in the file)
game_level = 3
enemies = ["Slime", "Hilichurl", "Fatui Agent"]


# * Function with a Local Scope example
def create_enemy():
    # new_enemy is created in this function's local scope and is only accessible here.
    if game_level < 5:
        new_enemy = enemies[0]  # Local variable, accessible only within create_enemy()

    # Accessing the local variable within the same function
    print(new_enemy)

# Calling the function will work because `new_enemy` is accessed within its scope
create_enemy()

# Attempting to access new_enemy outside of create_enemy() would raise a NameError:
# print(new_enemy)  # ! Uncommenting this will raise an error, as new_enemy is out of scope
