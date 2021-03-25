"""
using a xmen hq cover found on google images

import colorgram

rgb_colors = []
colors = colorgram.extract('Day 018/xmen.jpg', 30) #if you are on windows make sure the path of the image is with /
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

print(rgb_colors)
"""
import turtle as t
from random import choice
color_list = [(95, 191, 219), (119, 87, 59), (225, 152, 63), (60, 96, 133), (229, 53, 90),
              (21, 37, 60), (249, 208, 49), (51, 36, 24), (191, 140, 44), (243, 230, 213), 
              (146, 63, 94), (49, 20, 32), (74, 107, 83), (35, 60, 103), (183, 135, 161), 
              (132, 175, 154), (20, 33, 24), (210, 81, 59), (232, 237, 235), (121, 212, 233), 
              (86, 124, 182), (126, 33, 61), (75, 154, 171), (83, 68, 35), (240, 228, 235), 
              (214, 230, 239), (117, 43, 30), (39, 80, 48), (93, 153, 113), (31, 77, 88)]


timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")
timmy.penup()
timmy.setpos(-250, 250)

y = 250
for _ in range(10):
    for _ in range(10):
        timmy.dot(20, choice(color_list))
        timmy.forward(50)
    y = y - 50
    timmy.setpos(-250, y)
timmy.hideturtle()
screen = t.Screen()
screen.exitonclick()