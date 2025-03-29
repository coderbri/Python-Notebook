import csv

# with open("weather_data.csv", mode="r") as weather_data_csv:
#     print(data)
#     data = weather_data_csv.readlines()

with open("weather_data.csv") as weather_data_file:
    data = csv.reader(weather_data_file)
    # print(data)
    temperatures = []
    for row in data:
        # print(row)
        if row[1] != "temp":
            temp = row[1]
            temperatures.append(int(temp))
    print(temperatures)     # [12, 14, 15, 14, 21, 22, 24]

