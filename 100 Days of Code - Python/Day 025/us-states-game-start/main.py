import pandas as pd
from turtle import Screen, Turtle
#organazing data
data = pd.read_csv("Day 025/us-states-game-start/50_states.csv", index_col = 0)
data = data.to_dict()

new_dict = {}
for names, x in data["x"].items():
    new_dict[names] = [x]

for names, y in data["y"].items():
   new_dict[names].append(y)

city_names = []
for names, values in new_dict.items():
    new_dict[names] = tuple(values)
    city_names.append(names)


#setting screen 
screen = Screen()
screen.bgpic("Day 025/us-states-game-start/blank_states_img.gif")
pen = Turtle()
pen.hideturtle()
pen.penup()

right_names = []
while len(right_names) < len(city_names):
    city = screen.textinput(title="city",prompt= "Name a city on the map to stop write 'stop': ")
    if new_dict.get(city):
        pen.goto(new_dict[city])
        right_names.append(city)
        pen.write(f"{city}", align = "center", font= ("Courier", 10, "normal"))
    if city == "stop":
        break

screen.exitonclick()