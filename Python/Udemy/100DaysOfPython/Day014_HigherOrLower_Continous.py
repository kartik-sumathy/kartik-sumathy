import random
from Day014_HigherOrLower_Data import data

# templist = random.choices(cardDeck,weights=None, cum_weights=None, k=count)

def get_random_data(data):
    return random.choice(data)

def format_data(user_data):
    formatted_data = f"{user_data['name']} is a {user_data['description']} from {user_data['country']}"
    return formatted_data

def compare_data(count_a, count_b):
    pass


optionA = get_random_data(data)
optionACount = optionA['follower_count']
optionB = get_random_data(data)
optionBCount = optionB['follower_count']

# print(optionACount)
# print(optionBCount)

print(f"{format_data(optionA)} vs {format_data(optionB)}")
userChoice = input('Input A or B')