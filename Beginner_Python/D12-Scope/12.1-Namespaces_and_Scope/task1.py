# * Global Variable (Global Namespace)
enemies = 1


# ? Function to show Local Scope with the same variable name
def increase_enemies():
    # Local Variable (Local Namespace inside the function)
    enemies = 2
    print(f"enemies inside function: {enemies}")


# ? Calling the function to see local vs. global scope in action
increase_enemies()
print(f"enemies outside function: {enemies}")  # Still 1, as global 'enemies' isn't changed


# * Local Scope: Variable only exists within `drink_potion`
def drink_potion():
    potion_strength = 2
    print(f"Potion strength inside function: {potion_strength}")


drink_potion()
# print(potion_strength)  # ! Uncommenting this will raise a NameError


# * Global Scope: Accessing global variable within a function
player_health = 10


def drink_potion2(health):
    # Global variable accessed inside the function
    print(f"Player Health before drinking: {player_health} pts.")
    potion_strength = 2
    health += potion_strength
    print(f"Player drank potion! New Health: {health} pts.")


drink_potion2(player_health)


# * Namespace Example: Nested functions and scope isolation
def game():
    # Local to `game`, but global to nested function `drink_potion3`
    game_level = 3

    def drink_potion3():
        potion_strength = 3  # Local to `drink_potion3`
        print(f"Game level: {game_level}")  # Accessible due to enclosing scope
        print(f"Potion strength inside nested function: {potion_strength}")

    # Call the nested function within `game()`
    drink_potion3()


# ? Call `game` to see the nested function in action
game()

# ? Trying to call `drink_potion3` outside `game` will raise an error
# drink_potion3()  # ! Uncommenting this will raise a NameError

"""Explanation
Global Scope: Variables like enemies and player_health are 
    declared at the top level and are accessible throughout the file.

Local Scope: Inside increase_enemies() and drink_potion(), 
    variables like enemies and potion_strength are local to 
    their respective functions and are not accessible outside.

Namespace: The game() function introduces a local namespace 
    with game_level accessible to any function nested within it, 
    like drink_potion3(). However, drink_potion3() itself is 
    only accessible within game(), showing how nested functions 
    create namespaces that isolate code.
"""
