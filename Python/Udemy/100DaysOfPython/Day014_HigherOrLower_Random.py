import random
from Day014_HigherOrLower_Data import data


# templist = random.choices(cardDeck,weights=None, cum_weights=None, k=count)

def get_random_person(count):
    rand_list = random.choices(range(len(data)), weights=None, cum_weights=None, k=count)
    data_list = []
    for i in range(len(rand_list)):
        data_list.append(data[rand_list[i]])
    print(data_list)
    return data_list


def print_details(user):
    user_description = f"{user['name']} is a {user['description']} from {user['country']}"
    return user_description


def get_follower_count(user):
    follower_count = user['follower_count']
    return follower_count


def follower_compare(left, right):
    if left > right:
        return True
    else:
        return False


def game(win_count, chosenList):
    for person in chosenList:
        print(print_details(person))
    userInput = input('Enter which side is higher, Left or Right').lower()
    if userInput == 'left':
        if follower_compare(chosenList[0]['follower_count'], chosenList[1]['follower_count']):
            win_count += 1
            chosenList.pop(1)
            chosenList.append(get_random_person(1)[0])
            print(chosenList)
            print(f"You Won, your win streak is {win_count}")
            return win_count
        else:
            print(f"You lost, your win streak is {win_count}")
            print(chosenList)
            win_count += 0
            return win_count
    elif userInput == 'right':
        if follower_compare(chosenList[1]['follower_count'], chosenList[0]['follower_count']):
            win_count += 1
            chosenList.pop(0)
            chosenList.append(get_random_person(1)[0])
            print(f"You Won, your win streak is {win_count}")
            return win_count
        else:
            print(f"You lost, your win streak is {win_count}")
            win_count += 0
            return win_count


print('Welcome to Higher or Lower')
GameList = get_random_person(2)
startCount = -1
gameCount = startCount + 1
while gameCount > startCount:
    gameCount = game(gameCount, GameList)
    startCount += 1
