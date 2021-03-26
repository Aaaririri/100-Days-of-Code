from turtle import Turtle, Screen, forward
snake = []
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
def init():
    pos = 0
    for i in range(3):
        snake.append(Turtle("square"))
        snake[i].penup()
        snake[i].color("blue", "blue")
        snake[i].goto(pos, 0)
        pos = pos - 20
    
def move_forward():
    for i in range(2,0,-1):
        snake_x = snake[i - 1].xcor()
        snake_y = snake[i - 1].ycor()
        snake[i].goto(snake_x, snake_y)
    snake[0].forward(20)
        
def arrow_up():
    snake[0].setheading(90)
    move_forward()
    

def arrow_down():
    snake[0].setheading(270)
    move_forward()


def arrow_left():
    snake[0].setheading(180)
    move_forward()
    

def arrow_right():
    snake[0].setheading(0)
    move_forward()
    


    

screen.exitonclick()