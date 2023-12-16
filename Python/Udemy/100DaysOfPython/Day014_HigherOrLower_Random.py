import random
from Day014_HigherOrLower_Data import data


# templist = random.choices(cardDeck,weights=None, cum_weights=None, k=count)

def get_random_person(count, length):
    return random.choices(range(length), weights=None, cum_weights=None, k=count)


def get_details(user_index):
    user_description = f"{data[user_index]['name']} is a {data[user_index]['description']} from {data[user_index]['country']}"
    return user_description


def get_follower_count(user_index):
    follower_count = data[user_index]['follower_count']
    return follower_count


def follower_compare(left, right):
    if left > right:
        return True
    else:
        return False


def game(win_count):
    numberOfChoices = len(data)
    chosenList = get_random_person(2, numberOfChoices)
    chosenDetails = []

    for person in chosenList:
        chosenDetails.append({"details": get_details(person), "follower_count": get_follower_count(person)})
    print(f"{chosenDetails[0]['details']} vs {chosenDetails[1]['details']}")
    userInput = input('Enter which side is higher, Left or Right').lower()
    if userInput == 'left':
        if follower_compare(chosenDetails[0]['follower_count'], chosenDetails[1]['follower_count']):
            win_count += 1
            print(f"You Won, your win streak is {win_count}")
            return win_count
        else:
            print(f"You lost, your win streak is {win_count}")
            win_count += 0
            return win_count
    elif userInput == 'right':
        if follower_compare(chosenDetails[1]['follower_count'], chosenDetails[0]['follower_count']):
            win_count += 1
            return (f"You Won, your win streak is {win_count}")
            return win_count
        else:
            print(f"You lost, your win streak is {win_count}")
            win_count += 0
            return win_count


print('Welcome to Higher or Lower')
startCount = -1
gameCount = startCount + 1
while gameCount > startCount:
    gameCount = game(gameCount)
    startCount += 1
