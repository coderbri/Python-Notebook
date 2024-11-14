# * Modifying Global Scope
enemies = 1

# ? This approach modifies a global variable, which can lead to unexpected side effects.
# ? It makes the function dependent on external state, making it harder to debug and reuse.
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

enemies2 = 1

# * This method is better because it avoids modifying the global scope.
# ? Instead, it takes `enemy` as an argument, making it self-contained and easier to reuse.
def increase_enemies2(enemy):
    print(f"enemies inside function: {enemy}")
    return enemy + 1

enemies2 = increase_enemies2(enemies2)
print(f"enemies outside function: {enemies2}")
