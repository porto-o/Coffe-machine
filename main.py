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
    "profit": 0
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def barista():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        print_report()
        barista()
    elif order == "admin off":
        print("Turning off the machine...")
        exit()
    else:
        water, milk, coffee = get_ingredients(order)
        if check_inventory(water, milk, coffee):
            if process_coins(order):
                make_coffee(order, water, milk, coffee)
        else:
            barista()


def get_ingredients(order):
    water = MENU[order]["ingredients"]["water"]
    coffee = MENU[order]["ingredients"]["coffee"]
    if not order == "espresso":
        milk = MENU[order]["ingredients"]["milk"]
        return water, milk, coffee
    else:
        return water, 0, coffee


def print_report():
    for resource in resources:
        print(f"{resource}: {resources.get(resource)}")


def check_inventory(water, milk, coffee):
    order_ingredients = {"water": water, "milk": milk, "coffee": coffee}
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def decrease_inventory(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


def process_coins(drink):
    count = 0
    drink_price = MENU[drink]["cost"]
    for coin in coins:
        amount = float(input(f"How many {coin}: "))
        count += coins[coin] * amount
    if count >= drink_price:
        change = round(count - drink_price)
        print(f"Here is your change: ${change}")
        resources["profit"] += drink_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        barista()


def make_coffee(order, water, milk, coffee):
    decrease_inventory(water, milk, coffee)
    print(f"Here is your {order}. Enjot it!!!")
    barista()


barista()
