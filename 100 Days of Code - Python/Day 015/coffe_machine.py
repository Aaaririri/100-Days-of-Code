MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def continue_oparations():
    to_continue = True
    if input("To turn 'off' click 'o' or 'r' for 'restart': ") == 'o':
        to_continue = False
    return to_continue

def make(drink):
    ingredients = MENU[drink]["ingredients"]
    for name, amount in ingredients.items():
        resources[name] =  resources[name] - amount


def drink_ingredients(drink):
    ingredients = MENU[drink]["ingredients"]
    for name, amount in ingredients.items():
        if amount > resources[name]:
            return False
    return True


def payment(drink):
    try:
        value = float(input("Insert your coins: "))
        drinks_value = MENU[drink]["cost"]
        if drinks_value <= value:
            print(f"Your change is $ { value - drinks_value}")
            return True
        else:
            return False
    except:
        print("Invalid payment")
        drink_choice()
        


def drink_choice(choice = True):
    if choice:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink  == 'espresso' or drink == 'latte' or drink == 'cappuccino':
            drink_payment = payment(drink)
            if drink_payment:
                drink_possible = drink_ingredients(drink)
                if drink_possible:
                    make(drink)
                    print("Here is your drink, have a nice day!")
                    if input("Do you want another drink 'y' or 'n': ") == 'y':
                        drink_choice()
                else:
                    print("There is not enought resources ate the coffe machine")
                    drink_choice(continue_oparations())
            else:
                print("You did not pay for the drink")
                drink_choice(continue_oparations())
        else:
            print("Invalid choice")
            drink_choice(continue_oparations())

    

drink_choice()