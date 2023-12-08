import random
from Day007_HangmanWordList import word_list

def getGuessedChar():
    guessedChar = input("Enter the guess:").lower()
    return guessedChar

#initial Setup

words = word_list
spaces = '_'
guessword = ''
word = random.choice(words)

#Get First Input

print('Welcome to Hangman, You have 6 Guesses, you lose on the 7th guess')
print('Your Word has: ', len(word), ' Characters')
guessword = spaces * len(word)
guesslist = [*guessword]
wordlist = [*word]
print(guesslist)
print(wordlist)

hangmanCount = 6

while hangmanCount >0:
    guess = getGuessedChar()
    found = False
    for i in range(len(wordlist)):
        element = wordlist[i]
        if element.lower() == guess:
            guesslist[i] = guess
            found = True
    if found:
        if not '_' in guesslist:
            print('You won the game')
            print(guesslist)
            break
        else:
            print('You are close')
            print(guesslist)
            print('Lives:',hangmanCount)
    else:    
        print('you lost a life')
        print(guesslist)
        hangmanCount -= 1
        print('Lives:',hangmanCount)













# print(spaces * len(word))

# for element in word:
#     print(element)
#     if element.lower() == charc:
#         print(True)
#     else:
#         print(False)


# hangmanCount = 6

# for i in range(hangmanCount):
#     print(i)