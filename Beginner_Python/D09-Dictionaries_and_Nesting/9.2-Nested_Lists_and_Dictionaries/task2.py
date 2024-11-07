# * Nesting a List Inside a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# * Printing a List Item from a Dictionary
print(travel_log["France"][1])  # Lille

# * Nested Lists
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])        # D

# * Nesting both Lists and Dictionaries
new_travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
print(new_travel_log["Germany"]["cities_visited"][2])
# Stuttgart
