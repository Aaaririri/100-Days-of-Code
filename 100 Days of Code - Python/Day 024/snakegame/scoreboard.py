from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

"""
opened the file using the relative path of the text file
"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day 024\snakegame\high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Record: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day 024\snakegame\high_score.txt", mode = "w") as file:
                file.write(str(self.high_score))
        self.score = 0 
        self.update_scoreboard()
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
