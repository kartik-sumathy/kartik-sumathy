from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from  money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_box = MoneyMachine()


def game():
    coffeeChoice = input(f'Enter your order: {coffee_menu.get_items()}').lower()
    while coffeeChoice != 'off':
        if coffeeChoice == 'report':
            coffee_maker.report()
            money_box.report()
            game()
        elif coffeeChoice in coffee_menu.get_items():
            coffee_order = coffee_menu.find_drink(coffeeChoice)
            resource_check = coffee_maker.is_resource_sufficient(coffee_order)
            if resource_check:
                moneyPaid = money_box.make_payment(coffee_order.cost)
                if moneyPaid:
                    coffee_maker.make_coffee(coffee_order)
                    money_box.report()
                    coffee_maker.report()
                    game()
        elif coffeeChoice != 'off':
            print('Invalid Input')
            game()
        elif userInput == 'off':
            money_box.report()
            coffee_maker.report()
            print('Machine Switched Off')
            exit()

game()

