"""
exercise made using the stating code on:
https://replit.com/@appbrewery/oop-coffee-machine-start
"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    try:
        choice = input(f"What would you like? ({options}): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
            is_payment_successful = money_machine.make_payment(drink.cost)
            if is_enough_ingredients: 
                if is_payment_successful:
                    coffee_maker.make_coffee(drink)
                else:
                    print("Not enought money to make the order")
            else:
                print("We are sorry to inform that we are out of resources")
    except AttributeError:
        print("Invalid choice")
    





