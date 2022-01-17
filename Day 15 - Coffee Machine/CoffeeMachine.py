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

money = 10


def print_report():
    """Prints a list of all available resources left in the machine as well as total profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print("Money: $" + str(money))


def resource_sufficient(given_resource):
    """Function that checks the value of the given resource against the total ingredients list. 
    Returns False if there is not enough."""
    for item in given_resource:
        if given_resource[item] >= resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def check_coins():
    """Returns total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.10
    total += int(input("How many Nickles?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total


def transaction_successful(money_recieved, drink_cost):
    """Returns True if enough money inserted, else False."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your change, ${change} in dollars.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry, not enough money.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources dictionary."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}!☕️")


machine_is_on = True

while machine_is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino?): ")

    if user_input == "off":
        machine_is_on = False

    if user_input == 'report':
        # A function can be called directly.
        print_report()

    else:
        # Assign variable to the user input that checks the above dictionary. If resource is sufficient
        # check for sufficient funds.
        drink = MENU[user_input]
        if resource_sufficient(drink['ingredients']):
            # A function call can be called directly (it holds whatever value is defined in the function).
            payment = check_coins()
            if transaction_successful(payment, drink['cost']):
                make_coffee(user_input, drink['ingredients'])
