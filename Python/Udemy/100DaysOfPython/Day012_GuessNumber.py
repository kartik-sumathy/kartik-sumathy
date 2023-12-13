import random

def compare_numbers(actual, guess):
    if actual == guess:
        return True
    elif guess > actual:
        print('Too big, Guess again')
        return False
    elif guess < actual:
        print('Too Small, Guess again')
        return False

def get_chances():
    Difficulty = input('Select Difficulty: Easy or Hard').lower()
    if Difficulty == 'easy':
        return 10
    elif Difficulty == 'hard':
        return 5

def game():

    NumberToGuess = random.randint(1,100)
    chance = 0
    chances = 0
    guess = 0

    print('Welcome to Guess the Number')

    chances = get_chances()

    while chance < chances:
        chance += 1
        guess = int(input("Enter your Guess"))
        if compare_numbers(NumberToGuess,guess):
            print(f"You Won, the number is {NumberToGuess}, you took {chance} chances to find")
            break
        else:
            print(f"You have {chances - chance} Chances")
            if chance == chances:
                print(f"You Lost, the number is {NumberToGuess}")


game()


