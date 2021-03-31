import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
new_player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(new_player.move_up, "Up")
screen.onkey(new_player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    score.display_score()
    for car in cars.all_cars:
        if car.distance(new_player) < 25:
            game_is_on = False
    
    if new_player.finish_line():
        cars.speed_up()
        score.up_score()


score.final_score()
screen.exitonclick()