print('welcome to treasure island')

direction  = input('Do you want to go left or right?').lower()

if direction == 'right':
    print('Game Over, You fell into river')
elif direction == 'left':
    swim = input('Great, you reached lake, Do you want to wait or swim').lower()
    if swim == 'swim':
        print('Game Over, You drowned')
    elif swim == 'wait':
        door = input('Great, you reached place, you have three doors, Red, Yellow, Blue').lower()
        if door == 'red':
            print('Game Over, You were killed by fire')
        elif door == 'blue':
            print('Game Over, You were killed by monster')
        elif door == 'yellow':
            print('You won the treasure')
        else:
            print('Game Over, Wrong Input')
    else:
        print('Game Over, Wrong Input')
else:
    print('Game Over, Wrong Input')