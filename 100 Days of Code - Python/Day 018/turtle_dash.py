from turtle import *
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DeepPink")
timmy.pencolor("Blue")
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
