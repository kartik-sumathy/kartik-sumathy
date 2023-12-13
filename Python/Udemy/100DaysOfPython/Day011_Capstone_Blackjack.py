import random

def getCards(count, cardList):
    """Appends the choice of card in the cardlist"""
    cardDeck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    templist = random.choices(cardDeck,weights=None, cum_weights=None, k=count)
    for i in range(len(templist)):
        cardList.append(templist[i])
    return cardList

def cardComparison(hTotal, cTotal, hList, cList):
    """Performs Blackjack Comparison"""
    if hTotal > 21:
        printTotals(hList, hTotal, cList, cTotal)
        print("Computer Won")
    elif cTotal > 21:
        printTotals(hList, hTotal, cList, cTotal)
        print("Human Won")
    elif hTotal == cTotal:
        printTotals(hList, hTotal, cList, cTotal)
        print("Draw")
    elif hTotal > cTotal:
        printTotals(hList, hTotal, cList, cTotal)
        print("Human Won")
    elif hTotal < cTotal:
        printTotals(hList, hTotal, cList, cTotal)
        print("Computer Won")

def cardhas11(cTotal, cList):
    if 11 in cList and cTotal > 21:
        cList.remove(11)
        cList.append(1)
        cTotal = getTotals(cList)
        return cTotal, cList
    else:
        cTotal = getTotals(cList)
        return cTotal, cList

def computerCardCheck(cTotal, cList):
    while cTotal < 17:
        cList = getCards(1, cList)
        cTotal = getTotals(cList)
        if 11 in cList and cTotal > 21:
            cTotal -= 10
    return cTotal, cList

def getDifference(total):
    return total - 21

def printTotals(human_cards, human_total, computer_cards, computer_total):
    print(f"Human Cards are {human_cards} and Sumtotal is {human_total}")
    print(f"Computer Cards are {computer_cards} and Sumtotal is {computer_total}")

def getTotals(cardList):
    sumTotal = 0
    for i in range(len(cardList)):
        sumTotal += cardList[i]
    return sumTotal


def Blackjack(play):
    if play == 'yes':
        HumanCards = []
        ComputerCards = []
        HumanCards = getCards(2, HumanCards)
        ComputerCards = getCards(2, ComputerCards)
        HumanCardTotal = getTotals(HumanCards)
        ComputerCardTotal = getTotals(ComputerCards)
        ComputerFirstCard = ComputerCards[0]
        print(f"Your Card Sum is {HumanCardTotal}")
        print(f"Computer's first card is {ComputerFirstCard}")
        humanChoice = input('Hit or Stand').lower()
        while humanChoice in ['hit', 'stand']:
            if humanChoice == 'stand':
                HumanCardTotal, HumanCards = cardhas11(HumanCardTotal, HumanCards)
                if ComputerCardTotal < 17:
                    ComputerCardTotal, ComputerCards = computerCardCheck(ComputerCardTotal,ComputerCards)
                    print(ComputerCards,ComputerCardTotal)
                    cardComparison(HumanCardTotal, ComputerCardTotal, HumanCards, ComputerCards)
                else:
                    cardComparison(HumanCardTotal, ComputerCardTotal, HumanCards, ComputerCards)
                    break
            elif humanChoice == 'hit':
                HumanCards = getCards(1, HumanCards)
                HumanCardTotal = getTotals(HumanCards)
                HumanCardTotal, HumanCards = cardhas11(HumanCardTotal, HumanCards)
                if ComputerCardTotal < 17:
                    ComputerCardTotal, ComputerCards = computerCardCheck(ComputerCardTotal,ComputerCards)
                    print(ComputerCards, ComputerCardTotal)
                    cardComparison(HumanCardTotal, ComputerCardTotal, HumanCards, ComputerCards)
                else:
                    cardComparison(HumanCardTotal, ComputerCardTotal, HumanCards, ComputerCards)
                    break
            else:
                humanChoice = input('Invalid Choice, Try again, Hit or Stand').lower()



print('Welcome to BlackJack')
play = input('Do you want to play BlackJack?').lower()
while play == 'yes':
    Blackjack(play)
    play = input('Do you want to play BlackJack?').lower()
print('Thank you for your time')
