from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("red","green")
        self.speed("fastest")
        coord_xy = (random.randint(-280, 280),random.randint(-280, 280))
        self.goto(coord_xy)
    
    def food_update(self):
        self.clear()
        coord_xy = (random.randint(-280, 280),random.randint(-280, 280))
        self.goto(coord_xy)