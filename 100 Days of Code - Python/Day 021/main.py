from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
xvalue = 600
yvalue = 600
screen.setup(width= xvalue, height= yvalue)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# init with the size of the screen you are using
my_snake = Snake(xvalue, yvalue)
my_food = Food()
my_score = ScoreBoard()

screen.listen()
screen.onkey(my_snake.arrow_right, "Right")
screen.onkey(my_snake.arrow_left, "Left")
screen.onkey(my_snake.arrow_up, "Up")
screen.onkey(my_snake.arrow_down, "Down")

in_game = True
while in_game:
    screen.update()
    time.sleep(0.1) 
    my_snake.move()
    if my_snake.invalid_move():
        """
        YOUR SNAKE ATE ITSELF
        OR YOU HIT THE WALL
        """
        in_game = False
    if my_snake.head.distance(my_food) < 15:
        my_score.score_update()
        my_snake.snake_update()
        my_food.food_update()
    
         
my_score.final_score()
screen.exitonclick()