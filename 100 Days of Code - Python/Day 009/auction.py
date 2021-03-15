"""
This program is meant to do a blind auction
In case you wanna use this code make sure to dowload art.py too and include in the same file as this code
art from:
https://repl.it/@appbrewery/blind-auction-start
Found the function to clear the screen here: 
https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
"""
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


def prize_winner(bids):
    higher_bid = ""
    for people in bids:
        if bids[people] > higher_bid:
            higher_bid = people
    print(f"The auctioned product goes to {higher_bid} for the $ {bids[higher_bid]} price")


def auction_bids():
    bids = {}
    new_bids = True
    print("Wellcome to de the Blind Auction.")
    while new_bids:
        name = input("Name of the bidder: ")
        value = input("Value of the bid: ")
        bids[name] = value 
        print(" Is there any new bidder ")
        is_there = input("'Yes' or 'No': ").lower()
        if is_there == 'yes':
            screen_clear()
            new_bids = True
        else:
            screen_clear()
            prize_winner(bids)
            new_bids = False


print(logo)
auction_bids()