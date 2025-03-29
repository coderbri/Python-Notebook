import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# * Convert Table to Dictionary
new_dict = data.to_dict()
# print(data_dict)

# * Convert Column Values to List
temp_list = data["temp"].to_list()
# print(temp_list)

# * Calculating Average without Pandas
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
average = calculate_average(temp_list)
print(f"The average is {average}.") # 17.428571428571427.

# * Calculating Average with Pandas
mean_temp = data["temp"].mean()
print(mean_temp)                    # 17.428571428571427

# * Retrieving Max Value
max_temp_val = data["temp"].max()
print(max_temp_val)     # 24

# * Get Data in Columns
print(data["condition"])
print(data.condition)

# * Get Data in Rows
print(data[data.day == "Monday"])

print(data[data.temp == max_temp_val])

# * Getting a Row's Data Based on an Attribute
monday = data[data.day == "Monday"]
print(monday.condition)

# Convert ˚C to ˚F
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)    # 53.6

# * Create a DataFrame from Scratch
new_dict = {
    "students": ["Ava", "Jane", "John"],
    "scores": [98, 77, 83]
}
new_data = pandas.DataFrame(new_dict)
# print(new_data)
new_data.to_csv("new_data.csv")
