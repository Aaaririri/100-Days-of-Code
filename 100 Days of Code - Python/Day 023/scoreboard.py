from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()


    def display_score(self):
        self.clear()
        self.goto(-100,240)
        self.pendown()
        self.write(f"Level: {self.level}", move=False, align="center", font= FONT)
        self.penup()
        
    def up_score(self):
        self.level += 1

    def final_score(self):
        self.clear()
        self.goto(-100,240)
        self.pendown()
        self.write(f"Level: {self.level}", move=False, align="center", font= FONT)
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write("GAME OVER", move=False, align="center", font= FONT)

