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

def resume(drink):
    ingredients = MENU[drink]["ingredients"]
    cost = MENU[drink]["cost"]
    for name, amount in ingredients.items():
        print(f"{name} : {amount}")
    print(f"cost : {cost}")

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

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def payment(drink):
    value = process_coins()
    drinks_value = MENU[drink]["cost"]
    if drinks_value <= value:
        print(f"Your change is $ { value - drinks_value}")
        return True
    else:
        return False

        

def drink_choice(choice):
    if choice:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink  == 'espresso' or drink == 'latte' or drink == 'cappuccino':
            resume(drink)
            drink_payment = payment(drink)
            if drink_payment:
                drink_possible = drink_ingredients(drink)
                if drink_possible:
                    make(drink)
                    print("Here is your drink, have a nice day!")
                else:
                    print("There is not enought resources ate the coffe machine")
                    
            else:
                print("You did not pay for the drink")
                
        else:
            print("Invalid choice")
        if input("Do you want another drink 'y' or 'n': ") == 'y':
            drink_choice(True)
        else:
            drink_choice(False)
    

    

drink_choice(True)