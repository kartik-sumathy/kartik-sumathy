# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

#BaseList
expenses = [['Jan',2200],['Feb',2350],['Mar',2600],['Apr',2130],['May',2190]]
#1.Compare Jan and Feb
if expenses[0][1] < expenses[1][1]:
    print('1. In February expenses were increased by Rs.', expenses[1][1]-expenses[0][1])
elif expenses[0][1] >= expenses[1][1]:
        print('In February expenses were not increased')
#2.Expenses in First Quarter
totalExpense = 0
for i in range(3):
    totalExpense += expenses[i][1]
print('2. The total expenses in the first quarter is Rs.', totalExpense)
#3.Check if you have spent exactly 2OOO Rs in any month
expenseFlag = False
expenseMonth = ''
for i in range(len(expenses)):
    if expenses[i][1] == 2000:
        expenseFlag = True
if expenseFlag:
    print('3. Yes, You have Spent 2000 in one of the months')
else:
    print('3. No, You have not Spent 2000 in any of the months')
#4.Add June value
expenses.append(['Jun',1980])
print('4. June Expenses added to the expense list', expenses)
#5.Make a correction
priorExpense = expenses[3][1]
expenses[3][1] -= 200
print('5. Expenses after the return', expenses[3][1], 'earlier it was', priorExpense)