import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option One
random_name = random.choice(friends)
print(random_name)

# Option 2
random_index = random.randint(0, 4)
print(friends[random_index])
