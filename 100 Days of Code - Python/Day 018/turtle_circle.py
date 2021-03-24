from math import ceil
import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

 
def draw_spiral(gap):
    for _ in range(ceil(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        heading = timmy.heading()
        timmy.setheading(heading + gap)

timmy = t.Turtle()
my_screen = t.Screen()
t.colormode(255)
timmy.speed("fastest")
timmy.shape("turtle")
gap = 1

draw_spiral(gap) 

my_screen.exitonclick()