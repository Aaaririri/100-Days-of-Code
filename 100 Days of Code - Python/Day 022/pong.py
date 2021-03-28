from turtle import Turtle 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
class Pong(Turtle):
    def __init__(self, i): 
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.goto(i)
        self.color("Pink")
        self.setheading(90)
        self.shapesize(stretch_len = 5, stretch_wid = 1)


    def key_up(self):    
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def key_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)