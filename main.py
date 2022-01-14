MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

money = 0


def check_resource(user_input, given_resource):
    if given_resource < [MENU][user_input]['ingredients'][given_resource]:
        return False
    else:
        # Deduct resources
        [MENU][user_input]['ingredients'][given_resource] -= given_resource
        return True


def check_money(user_input):
    quarters = input(int("How many quarters?: "))
    dimes = input(int("How many dimes?: "))
    nickels = input(int("How many nickels?: "))
    pennies = input(int("How many pennies?: "))

    money_inserted = (quarters * .25) + (dimes * .10) + \
        (nickels * .05) + (pennies * .01)

    if money_inserted < MENU[user_input]['cost']:
        print("Sorry that's not enough money. Money refunded")
        return False

    elif money_inserted > MENU[user_input]['cost']:
        change = money_inserted - MENU['espresso']['cost']
        money += MENU[user_input]['cost']
        print(f"Here is ${change} dollars in change")
        return False
    else:
        money += money_inserted
        return True


machine_is_on = True
while machine_is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino?): ")
    if user_input == "off":
        machine_is_on = False
    if user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print("Money: $" + str(money))

    if user_input == "espresso":
        if check_resource(user_input, 'water') == False:
            print("Sorry there is not enough water")
        if check_resource(user_input, 'coffee') == False:
            print("Sorry there is not enough coffee")

        elif check_money(user_input) == True:
            print(f"Here is your {user_input}. Enjoy!")

    if user_input == "latte":
        if check_resource(user_input, 'water') == False:
            print("Sorry there is not enough water")
        if check_resource(user_input, 'milk') == False:
            print("Sorry there is not enough milk")
        if check_resource(user_input, 'coffee') == False:
            print("Sorry there is not enough coffee")

        elif check_money(user_input) == True:
            print("Here is your {user_input}. Enjoy!")

    if user_input == "cappuccino":
        if check_resource(user_input, 'water') == False:
            print("Sorry there is not enough water")
        if check_resource(user_input, 'milk') == False:
            print("Sorry there is not enough milk")
        if check_resource(user_input, 'coffee') == False:
            print("Sorry there is not enough coffee")

        elif check_money(user_input) == True:
            print(f"Here is your {user_input}. Enjoy!")
