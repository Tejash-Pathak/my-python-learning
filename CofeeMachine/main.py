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


def resource(object_ingredient):
    """Checks If the resources are sufficient"""
    for amount in object_ingredient:
        if object_ingredient[amount] >= resources[amount]:
            print(f"Sorry there is not enough {amount}")
            return False
    return True


def change():
    """Calculates the total of the coins inserted"""
    print("Please insert coins")
    total = int(input("No of Quarters: ")) * 0.25
    total += int(input("No of Dimes: ")) * 0.10
    total += int(input("No of Nickels: ")) * 0.05
    total += int(input("No of Pennies: ")) * 0.01
    return total


def transaction_success(money_paid, drink_cost):
    """Will check if the money is accepted"""
    if money_paid >= drink_cost:
        cashback = round(money_paid-drink_cost, 2)
        print(f"Here is ${cashback} in change")
        global money
        money += drink_cost
        return True
    else:
        print("That is not enough money, money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Makes the coffee"""
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}. Enjoy ☕☕")


money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}
maintenance = False
# TODO: 1. print report
while not maintenance:
    COFEE = input("What would you like, Sir or Ma'am? (espresso/latte/cappuccino):")
    if COFEE == "report":
        print(f"Water: {resources['water']}ml, \nMilk: {resources['milk']}ml, \nCofee: {resources['coffee']}gm, \n"
              f"Money: ${money}")
    elif COFEE == "off":
        maintenance = True
    else:
        coffee = MENU[COFEE]
    # TODO: 2.resources sufficient
        if resource(coffee['ingredients']):
            paid = change()
            if transaction_success(paid, coffee['cost']):
                make_coffee(COFEE, coffee)

