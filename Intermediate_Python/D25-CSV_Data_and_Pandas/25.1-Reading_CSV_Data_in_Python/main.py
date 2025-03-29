import pandas

# * Retrieve Table
data = pandas.read_csv("weather_data.csv")
print(data)

# * Retrieve Column
print(data["temp"])
