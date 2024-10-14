states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                    "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                    "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                    "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america)

# * Length of a List
num_of_states = len(states_of_america)  # Indexes: 50 -> 49
print(num_of_states)                    # 50

# print(states_of_america[num_of_states])   # ! IndexError: list index out of range
print(states_of_america[num_of_states - 1]) # Hawaii

# * Nested Lists
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# * Accessing Indexes of a Nested List
#         list_index, index
print(dirty_dozen[0][3])    # Grapes
print(dirty_dozen[1][0])    # Spinach
