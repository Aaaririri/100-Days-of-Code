from turtle import *
import random

timmy = Turtle()
my_screen = Screen()
color_list = ["DeepPink","Blue","brown","coral","DarkBlue","hotpink", "indianRed1", "gold", "ForestGreen", "magenta", "OrangeRed"]

def run_turtle():
    color_choice = random.choice(color_list)
    timmy.color(color_choice)
    timmy.pencolor(color_choice)
    timmy.forward(100)
    timmy.right(360/x)


timmy.penup()
timmy.setpos(-50, 200)
timmy.shape("turtle")
timmy.pendown()

x = 3
while x < 15:
    for _ in range(x):
       run_turtle()
    x += 1


my_screen.exitonclick()