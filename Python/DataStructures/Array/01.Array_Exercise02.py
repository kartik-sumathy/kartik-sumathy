#heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

#------------------------------------
#BaseList
heros =['spider man','thor','hulk','iron man','captain america']

#Get Length
print('1. The total heros are', len(heros))

#Add Black Panther to the list 
heros.append('black panther')
print('2. The added hero is ', heros[len(heros)-1])

# Remove black panther from the list and add it after hulk
heros.remove(heros[len(heros)-1])
print('3. The updated heros are ', heros)
for i in range(len(heros)):
    if heros[i]=='hulk':
        heros.insert(i+1,'black panther')
print('3. The updated heros are ', heros)

# Remove Hulk and Thor, Replace with Strange
heros[1:3]=['doctor strange']
print('4. The updated heros are, ', heros)

# Sort
heros.sort()
print('5. The updated heros are, ', heros)
