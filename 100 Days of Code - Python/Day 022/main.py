from turtle import Screen
from pong import Pong
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")

my_pong = Pong((350, 0))
my_pong2 = Pong((-350, 0))
my_ball = Ball()
my_ball.init_ball()
my_score = ScoreBoard()
screen.tracer(0)
screen.listen()
screen.onkey(my_pong.key_up, "Up")
screen.onkey(my_pong.key_down, "Down")
screen.onkey(my_pong2.key_up, "w")
screen.onkey(my_pong2.key_down, "s")

in_game = True
while in_game:
    screen.update()
    time.sleep(0.1) 
    my_ball.move_ball()  

    if my_ball.distance(my_pong) < 50 and my_ball.xcor() > 320 or my_ball.distance(my_pong2) < 50 and my_ball.xcor() < -320:
        my_ball.swich_directionsx()

    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.swich_directionsy()

    if my_ball.xcor() <= -360:
        my_score.score_update(0)
        my_ball.goto(0,0)
        my_ball.init_ball()

    if my_ball.xcor() >= 360:
        my_score.score_update(1)
        my_ball.goto(0,0)
        my_ball.init_ball()
    
screen.exitonclick()