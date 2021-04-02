"""
csv stands for comma separated values
"""
import csv
from prettytable import PrettyTable
#using prettytable and csv
table = PrettyTable()
with open("Day 025/weather_data.csv") as data_file:
    data = csv.reader(data_file) 
    n = -1
    for row in data:
        n += 1
        if n == 0:
            table.field_names = row
        else:
            table.add_rows([row])


print(table)
#using pandas
import pandas as pd
data = pd.read_csv("Day 025/weather_data.csv")
print(data)

#average of temperatures
data_average = data["temp"].mean()
print(data_average)

#other option to the average 
data_list = data["temp"].to_list()
data_average = sum(data_list)/len(data_list)
print(data_average)

#another option to the average 
import statistics
data_average = statistics.mean(data_list)
print(data_average)