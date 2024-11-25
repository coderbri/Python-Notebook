from prettytable import PrettyTable
#     module            class name

# * 1. Construct object from class.
table = PrettyTable()

# 2. Call methods.
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

'''
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+
'''

# 3. Call Attributes
print(table.align)  # {'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
table.align = "l"
print(table.align)  # {'base_align_value': 'c', 'Pokemon Name': 'l', 'Type': 'l'}
print(table)

'''
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+
'''
