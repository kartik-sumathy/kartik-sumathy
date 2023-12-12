from os import system


def calcAdd(n1, n2):
    """Adds two numbers"""
    return n1 + n2


def calcSub(n1, n2):
    """Subtracts two numbers"""
    return n1 - n2


def calcMul(n1, n2):
    """Multiplies two numbers"""
    return n1 * n2


def calcDiv(n1, n2):
    """Divides two numbers"""
    return n1 / n2


dictOperations = {
    '+': calcAdd,
    '-': calcSub,
    '*': calcMul,
    "/": calcDiv,
}

def calculator():

    proceed = 'no'

    while proceed != 'Exit'.lower():
        if proceed == 'no'.lower():
            system('clear')
            num1 = float(input('Enter the first number'))
            num2 = float(input('Enter the second number'))
        elif proceed == 'yes'.lower():
            num1 = result
            num2 = float(input('Enter the second number'))

        for symbol in dictOperations:
            print(symbol)

        selOper = input('Select the operator from the list')

        result = dictOperations[selOper](num1, num2)

        print(f"{num1} {selOper} {num2} = {result}")

        proceed = input('Continue = Yes, or No, Exit').lower()


calculator()