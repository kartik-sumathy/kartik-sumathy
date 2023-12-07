import random

rps_h = int(input('Rock - 0; Paper - 1; Scissors - 2'))

if rps_h > 2 or rps_h < 0:
    print('Invalid Entry')
else:
    rps_c = random.randint(0,2)
    if rps_h == rps_c:
        print('Draw')
    elif rps_h == 0 and rps_c == 2:
        print('Human Wins')
    elif rps_c == 0 and rps_h == 2:
        print('Computer Wins')
    elif rps_h == 2 and rps_c == 1:
        print('Human Wins')
    elif rps_c == 2 and rps_h == 1:
        print('Computer Wins')
    elif rps_h == 1 and rps_c == 0:
        print('Human Wins')
    elif rps_c == 1 and rps_h == 0:
        print('Computer Wins')


