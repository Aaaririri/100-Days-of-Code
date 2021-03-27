from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        self.s = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score = {self.s}", move=False, align="center", font=("Arial", 15, "normal"))

    def score_update(self):
        self.s += 1 
        self.clear()
        self.write(f"Score = {self.s}", move=False, align="center", font=("Arial", 15, "normal"))

    def final_score(self):
        self.clear()
        self.write(f"Final Score = {self.s}", move=False, align="center", font=("Arial", 15, "normal"))
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 20, "normal"))