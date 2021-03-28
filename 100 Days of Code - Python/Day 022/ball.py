from turtle import Turtle
import random
START = [45, 135, 225, 315]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 1, stretch_wid = 1)
        self.color("red","blue")
        coord_xy = (0, 0)
        self.goto(coord_xy)
        self.x_move = 10
        self.y_move = 10
    
    def move_ball(self):
        cordx = self.xcor() + self.x_move
        cordy = self.ycor() + self.y_move
        self.goto(cordx, cordy)

    def init_ball(self):
        self.setheading(random.choice(START))
    
    def swich_directionsy(self):
        self.y_move *= -1
    
    def swich_directionsx(self):
        self.x_move *= -1
