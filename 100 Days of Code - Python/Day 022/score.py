from turtle import Turtle
LINE = 30
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0,0]
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write("SCORE", move=False, align="center", font=("Arial", 15, "normal"))
        self.goto(0, 250)
        self.write(f"{self.score[0]} x {self.score[1]}", move=False, align="center", font=("Arial", 15, "normal"))
        self.draw_lines()

    def draw_lines(self):
        self.pencolor("white")
        self.penup()
        self.setheading(270)
        self.goto(-360, 300)
        self.pendown()
        for _ in range(LINE):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()
        self.goto(360, 300)
        self.pendown()
        for _ in range(LINE):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()

    def score_update(self, pos):
        self.score[pos] += 1 
        self.clear()
        self.draw_lines()
        self.goto(0, 270)
        self.write("SCORE", move=False, align="center", font=("Arial", 15, "normal"))
        self.goto(0, 250)
        self.write(f"{self.score[0]} x {self.score[1]}", move=False, align="center", font=("Arial", 15, "normal"))