#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

listLength = int(input('Enter the list length ?'))
oddList = []

for i in range(listLength):
    if i % 2 != 0:
        oddList.append(i)


print(oddList)