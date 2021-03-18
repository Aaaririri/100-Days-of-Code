import random
import os
from time import sleep
from art import logo

# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   
sleep(5)

cards = ['1','2','3','4','5','6','7','8','9','10','Q','J','K']
values = [1,2,3,4,5,6,7,8,9,10,10,10,10]

def comp_play():
    deque = values.copy()
    deque_choice = []
    modifier = [0,1]
    while sum(deque_choice) < 21:
        novo_card = random.choice(deque)
        if novo_card== 1:
            deque_aux = [1,11]
            novo_card= random.choice(deque_aux)
        deque_choice.append(novo_card)
    if random.choice(modifier) == 1:
        deque_choice.pop(len(deque_choice)-1)
    return deque_choice



def your_play():
    screen_clear()
    print(logo)
    deque = values.copy()
    deque_choice = []
    modifier = [0,1,2,3]
    deque_aux = [1,11]
    to_continue = True
    while to_continue:
        if input("Do you want to pich a card 'y' or 'n':") == 'y':
            novo_card = random.choice(deque)
            if novo_card == 10:
                print(f'You pushed:{cards[9 + random.choice(modifier)]} value {novo_card }')
            else:
                print(f'You pushed:{cards[values.index(novo_card)]} value {novo_card }')
            if novo_card  == 1:
                try:
                    novo_card = int(input("Do you want 1 or 11: "))
                    if novo_card != 1 and novo_card != 11:
                        print("Please don't cheat if you do we gonna choose for you:")
                        novo_card = random.choice(deque_aux)
                        print(f"Your new value is: {novo_card}")
                except ValueError:
                    print("Invalid input.")
                    print("Please don't cheat if you do we gonna choose for you:")
                    novo_card = random.choice(deque_aux)
                    print(f"Your new value is: {novo_card}")
            deque_choice.append(novo_card) 
            print(f"Your hand {deque_choice}")
        else:
            to_continue = False
    return deque_choice

def who_wins(comp, player1):
    screen_clear()
    print(logo)
    player1 = last_ajust(player1)
    print(f"Last version of player's 1 deque: {player1}")
    print(f"Sum of the computer's cards: {sum(comp)}")
    print(f"Sum of my cards: {sum(player1)}")
    if sum(comp) > 21 and sum(player1) > 21:
        print("No winners.")
    elif sum(player1) > 21:
        print("You lose pass 21, computer wins.")
    elif sum(comp) > 21:
        print("Computer loses pass 21, you win.")
    else:
        if sum(comp) == sum(player1):
            print("You and Computer wins")
        elif sum(comp) > sum(player1):
            print("Computer wins")
        else:
            print("You Win")
    
def last_ajust(player1):
    if 11 in player1 and sum(player1) > 21:
        player1.remove(11)
        player1.append(1)
    return player1



who_wins(comp_play(),your_play())