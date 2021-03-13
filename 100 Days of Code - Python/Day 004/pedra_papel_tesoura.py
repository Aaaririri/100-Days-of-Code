#Day 4: Rock Paper Scissors
"""
The main goal is to create a simple Rock, Paper, Scissors game.
"""
import random 
print("Wellcome to This Big Event It's Time for Rock, Paper, Scissors")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
invalid = "You Can't Do That"
moves = [rock,paper,scissors, invalid]
computers_move = moves[random.randint(0,2)]
your_move = input("rock, paper or scissors: ")
if your_move == 'rock':
    your_move = moves[0]
elif your_move == 'paper':
    your_move = moves[1]
elif your_move == 'scissors':
    your_move = moves[2]
else:
    your_move = moves[3]

if your_move == computers_move:
    who_wins = "Tie"
elif your_move == rock and computers_move == scissors:
    who_wins = "You Win"
elif your_move == paper and computers_move == rock:
    who_wins = "You Win"
elif your_move == scissors and computers_move == paper:
    who_wins = "You Win"
else:
    who_wins ="Computer Wins"

print(your_move)
print(computers_move)
print(who_wins)