
print('welcome to the trip calculator')

totalBill = int(input('Enter the Total Bill Amount'))
totalFriends = int(input('Enter the number of friends at dinner'))
tipPercentage = int(input('Enter Tip Percentage within 5 to 15'))/100

individualShare = (totalBill+(totalBill*tipPercentage))/totalFriends

print(individualShare)

if totalBill > 0:
    if totalFriends > 1:
        if tipPercentage*100 > 5:
            individualShare = (totalBill+(totalBill*tipPercentage))/totalFriends
            print(f"Individual Share is: {individualShare}")




