from turtle import Turtle, Screen

brush = Turtle()
screen = Screen()

def w_move():
    brush.forward(10)

def s_move():
    brush.backward(10)

def d_turn():
    brush.right(brush.heading()+5)

def a_turn():
    brush.left(brush.heading()+5)

def clear():
    screen.resetscreen()

screen.listen()
screen.onkey(w_move, "w")
screen.onkey(s_move, "s")
screen.onkey(d_turn, "d")
screen.onkey(a_turn, "a")
screen.onkey(clear, "c")
screen.exitonclick()