import random
import my_module

# * Randomization
random_integer = random.randint(1, 10)
print(random_integer)

# * Importing from Module
print(my_module.my_favorite_number)

# * Generating Random Floating Point Number
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# * Generating Random Floating Point Number with .uniform()
random_float = random.uniform(1, 10)
print(random_float)

# * Challenge
print("\n=== CHALLENGE ===")

random_heads_or_tails = random.randint(0, 1)
# print(random_heads_or_tails)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
