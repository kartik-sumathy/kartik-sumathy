from os import system



# Day009


# Student Grades

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
#
# for score in student_scores:
#     if student_scores[score] > 90:
#         student_grades[score] = 'Outstanding'
#     elif 80 < student_scores[score] < 91:
#         student_grades[score] = 'Exceeds Expectations'
#     elif 70 < student_scores[score] < 81:
#         student_grades[score] = 'Acceptable'
#     elif student_scores[score] < 70:
#         student_grades[score] = "Fail"
#
# print(student_grades)

#system('clear')

print('Welcome to the Auction')
auctionList = {}
auctionContinue = 'yes'
highest_bid =0
while auctionContinue == 'yes':
    userName = input('Enter your name')
    bidAmount = int(input('Enter bid amount'))
    auctionList[userName] = bidAmount
    auctionContinue = input('Type yes to continue, Type No to Complete Auction ')
    if auctionContinue == 'yes':
        system('clear')
    elif auctionContinue == 'no':
        for bid in auctionList:
            if highest_bid < auctionList[bid]:
                highest_bid = auctionList[bid]
                winner = bid
print(f"The Winner is {winner} and the winning bid is {highest_bid}")





