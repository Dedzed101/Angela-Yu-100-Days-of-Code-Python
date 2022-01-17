from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mu = Menu()
mm = MoneyMachine()
machine_is_on = True
while machine_is_on:
    choice = input("What would you like? (latte/espresso/cappucccino): ")

    if choice == 'off':
        machine_is_on = False

    if choice == 'report':
        cm.report()

    else:
        drink = mu.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            mm.make_payment(drink.cost)
            cm.make_coffee(drink)
