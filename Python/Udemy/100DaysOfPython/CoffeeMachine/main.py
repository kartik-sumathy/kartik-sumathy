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

receipts = 0.0

resources = {
    "water": 240,
    "milk": 200,
    "coffee": 100,
}

coin_types = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}


def print_resources(stock, money):
    water = stock['water']
    milk = stock['milk']
    coffee = stock['coffee']
    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}\n')


def check_resources(stock, requirement):
    status = []
    for ingredient in requirement:
        print(ingredient, stock[ingredient])
        if requirement[ingredient] > stock[ingredient]:
            print(f'Sorry, there is not enough {ingredient}')
            return False
    return True

def deduct_resources(stock, requirement):
    for ingredient in requirement:
        stock[ingredient] = stock[ingredient] - requirement[ingredient]
    return stock

def calculate_coins(coins,cost):
    total = 0.0
    product = 0.0
    count = 0
    for coin in coins:
        count = int(input(f'insert the {coin}'))
        product = count * coins[coin]
        total += product
        refund = 0.0
    if total <= cost:
        print(f'{total} is less than the {cost}, Money Refunded ')
        return False
    else:
        refund = total - cost
        print(f'Coffee being dispensed, Please collect the change - {refund}')
        return True


def CoffeeMachine(resources, receipts):
    session_resources = resources
    session_receipts = receipts
    userInputs = ['report', 'espresso', 'latte', 'cappuccino']
    userInput = input('What would you like to have, 1. espresso, 2. Latte, 3. Cappuccino').lower()
    while userInput != 'off':
        if userInput == 'report':
            print_resources(session_resources, session_receipts)
            CoffeeMachine(session_resources, session_receipts)
        elif userInput in userInputs:
            resource_check = check_resources(resources, MENU[userInput]['ingredients'])
            if resource_check:
                money_check = calculate_coins(coin_types, MENU[userInput]['cost'])
                if money_check:
                    session_receipts += MENU[userInput]['cost']
                    session_resources = deduct_resources(session_resources,MENU[userInput]['ingredients'])
                    CoffeeMachine(session_resources, session_receipts)
                else:
                    CoffeeMachine(session_resources,session_receipts)
            else:
                CoffeeMachine(session_resources, session_receipts)
        elif userInput != 'off':
            print('Invalid Input')
            CoffeeMachine(session_resources,session_receipts)
    if userInput == 'off':
        print_resources(session_resources, session_receipts)
        print('Machine Switched Off')
        exit()


CoffeeMachine(resources, receipts)

# TODO Check the corner cases