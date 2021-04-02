"""
Primary Fur Color
"""
import pandas as pd
data = pd.read_csv("Day 025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_count = data["Primary Fur Color"].value_counts()
fur_count = fur_count.to_dict()

data_count = {
                "Fur Color":[],
                "Amount":[]
                }

for name, value in fur_count.items():
    data_count["Fur Color"].append(name)
    data_count["Amount"].append(value)

new_data = pd.DataFrame(data_count)
new_data.to_csv("Day 025/fur_color.csv")