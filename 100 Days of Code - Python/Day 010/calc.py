import os
from time import sleep
from collections import defaultdict 
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



def add(a,b):
    return a + b
    
def sub(a,b):
    return a - b
    
def div(a,b):
    return a / b
            

def mult(a,b):
    return a * b
   
def invalid(a,b):
    return "Invalid Operation"

operations = defaultdict(lambda: invalid)
operations["+"] = add
operations["-"] = sub
operations["*"] = mult
operations["/"] = div

#operations = defaultdict(lambda: invalid)
def calculator():
    print(logo)
    is_running = True
    while is_running:
        print("Let's calculate:")
        op = input("What operation you want to make \n adicion: '+' subtraction: '-' multiplication: '*' or division '/':  ")
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            print(f"Result: {operations[op](a,b)}")
        except ValueError:
            print("Invalid input.")
        except:
            print("Operation not possible.")

        if input("Do you want to continue 'yes' or 'no': ").lower() != 'yes':
            is_running = False


        screen_clear()

calculator()