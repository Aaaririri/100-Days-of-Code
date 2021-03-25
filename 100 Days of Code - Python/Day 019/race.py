from turtle import Turtle, Screen, exitonclick
from random import randint
racers = []
colors = ["blue","red","yellow","pink","green"]
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="who will win?",prompt= "('blue','red','yellow','pink','green'): ")

y = 200
brush = Turtle()
brush.penup()
brush.goto(200,200)

for i in range(5):
    racers.append(Turtle(shape="turtle"))
    racers[i].color(colors[i])
    racers[i].penup()
    y = y - 50 
    racers[i].setpos(-200, y)

brush.pendown()
brush.goto(200,y - 50)
brush.hideturtle()
brush.penup()
brush.goto(-50,0)

is_end = True
if user_bet:
    is_end = False

while not is_end:
    for t in racers:
        t.forward(randint(0,10))
        if t.xcor() > 200:
            win = t.pencolor()
            is_end = True
            brush.pendown()
            if user_bet == win:
                brush.write("You bet right", move=False, align="left", font=("Arial", 12, "normal"))
            else:
                brush.write("You bet wrong", move=False, align="left", font=("Arial", 12, "normal"))

                
                
screen.exitonclick()
