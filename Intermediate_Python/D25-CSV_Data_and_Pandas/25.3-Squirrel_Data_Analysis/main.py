import pandas

# Read the squirrel census data from CSV
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.")

# TODO: Create a DataFrame summarizing the count of squirrels based on their primary fur color.
# The output should list each fur color along with the corresponding total count.
# Fur colors in the dataset: Gray, Cinnamon, Black.

# * 1. Filter the dataset to retrieve only squirrels of each fur color.
gray_squirrels = data[data["Primary Fur Color"]== "Gray"]
# print(gray_squirrels)
# ? Displays a truncated table containing only rows where the squirrel's primary fur color is Gray.
# ? The total number of rows at the bottom represents the count of gray squirrels.

# * 2. Count the number of squirrels for each fur color.
# ? Using `len()` to determine the count of each primary fur color
gray_squirrels_count = len(data[data["Primary Fur Color"]== "Gray"])
print(gray_squirrels_count)         # Output: 2473

red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"]== "Black"])
print(red_squirrels_count)          # Output: 392
print(black_squirrels_count)        # Output: 103

# * 3. Create a dictionary to store the fur color data and convert it into a DataFrame
fur_color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

fur_color_df = pandas.DataFrame(fur_color_dict)
print(fur_color_df)
# ? This should display a DataFrame containing fur colors and their respective counts.
# ? Once confirmed, we export the DataFrame to a CSV file.

fur_color_df.to_csv("squirrel_count.csv")
