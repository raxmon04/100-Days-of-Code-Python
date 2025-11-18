with open("/mnt/d/Git/python/025_USStateGame/day-25-start/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

# ================================================================================================================ #

import csv
with open("/mnt/d/Git/python/025_USStateGame/day-25-start/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# ================================================================================================================ #

import pandas

data = pandas.read_csv("/mnt/d/Git/python/025_USStateGame/day-25-start/weather_data.csv")
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(sum(temp_list))

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_F = monday.temp[0] * 9/5 + 32
print(monday_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],

}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")