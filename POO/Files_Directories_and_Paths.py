# ! DAY 24 Snake game has code example

# OPEN, CLOSE, READ, APPEND AND WRITE FILES
# The first method closes the file when you finish
# If you don't add the mode its in only reading
# 'w' stands for writing and 'a' stands for append in case you only want to add something
# If the file does not exist and is in write mode, one new file would be created
with open("my_file.txt", mode="w") as file:
    contents = file.read()
    file.write("")

file = open("my_file.txt")
file.close()

# SOME OTHER METHODS
variable = "Carlos"
PLACEHOLDER = "[name]"

variable.strip()  # removes all the spaces in the beginning and at the end
file.readlines()  # returns all the lines in the file by lines
file.replace(PLACEHOLDER, variable)

# READING CSD DATA
# information separated by commas

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
type(data)  # dataframe is a table that then it's separated by commas
# the series is every column
temp_list = data["temp"].to_list()

average = sum(temp_list) / len(temp_list)
print(data["temp"].mean())  # this 2 lines makes the exact same thing
print(data["data"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")  # add the file where you want to create the csv file 
