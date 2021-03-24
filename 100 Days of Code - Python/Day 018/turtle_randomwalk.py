import turtle as t
import random

timmy = t.Turtle()
my_screen = t.Screen()
color_list = ["DeepPink", "Blue", "brown", "coral", "DarkBlue", "hotpink", "indianRed1", "gold", "ForestGreen", "magenta", "OrangeRed"]
angle_list = [0, 90, 180, 270]

def draw_line():
    timmy.color(random.choice(color_list))
    timmy.pencolor(random.choice(color_list))
    timmy.forward(30)
    timmy.setheading(random.choice(angle_list))

timmy.shape("turtle")
timmy.speed("fastest")
timmy.pensize(15)

for _ in range(200):
    draw_line()

my_screen.exitonclick()