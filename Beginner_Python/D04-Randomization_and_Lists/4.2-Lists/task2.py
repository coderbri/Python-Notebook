states_of_america= ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# * Accessing Items
print(states_of_america[0])      # Delaware
print(states_of_america[-1])     # Hawaii

# * Modifying Items
print(states_of_america[1])             # Pennsylvania
states_of_america[1] = "Pencilvania"
print(states_of_america[1])             # Pencilvania

# * Appending to a List
states_of_america.append("Transylvania")
print(states_of_america)                # [..., ..., 'Transylvania']
print(states_of_america[50])            # Transylvania

# * Extending a List
states_of_america.extend(["Bermuda Triangle, Netherworld"])
print(states_of_america)                # [..., ..., 'Bermuda Triangle, Netherworld']
