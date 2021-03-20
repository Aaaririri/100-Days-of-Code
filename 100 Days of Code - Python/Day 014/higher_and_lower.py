from game_data import data
import random
import os
from time import sleep

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
""" 

# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   
sleep(5)


def info(first_person, second_person):
    for name, information in first_person.items():
        print(f"{name} : {information}")
    print(vs)
    for name, information in second_person.items():
        print(f"{name} : {information}")


def higher_lower(first_person, second_person, points):
    choice = input("Who's higher 1 or 2: ")
    if choice == "1" and first_person['follower_count'] > second_person['follower_count']:
        screen_clear()
        info(first_person, second_person)
        print("Right!")
        points += 1
        print(f"your score: {points}")
        people(points)

    elif choice == "2" and first_person['follower_count'] < second_person['follower_count']:
        screen_clear()
        info(first_person, second_person)
        print("Right!")
        points += 1
        print(f"your score: {points}")
        people(points)

    else:
        screen_clear()
        info(first_person, second_person)
        print("Wrong!")
        print(f"Your final score is {points} points")


def people(points):
    first_person = random.choice(data)
    second_person = first_person
    while second_person == first_person:
        second_person = random.choice(data) 
    
    print(f'{first_person["name"]}, {first_person["description"]}')
    print(vs)
    print(f'{second_person["name"]}, {second_person["description"]}')
    higher_lower(first_person, second_person, points)

def play():
    print(logo)
    to_play = True
    points = 0
    while to_play:
        people(points)
        if input("Do you wanna play again 'y' or 'n': ") != 'y':
            to_play = False
        screen_clear()

play()