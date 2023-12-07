import random

strSymbols = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"

noChar = int(input('Enter Password length'))-1

noSym = int(input('No of Symbols'))

noNum = int(input('No of Numbers'))

noChar = noChar-(noSym+noNum)

pwd = []
1
while len(pwd) <= noChar-1:
    for i in range(noChar):
        ranAlphaCaps = random.randint(65,90)
        ranAlphaSmall = random.randint(97,122)
        Toss = random.randint(0,1)
        if Toss == 1:
            pwd.append(chr(ranAlphaCaps))
        else:
            pwd.append(chr(ranAlphaSmall))

    for i in range(noSym):
        ranSym = random.randint(0,31)
        pwd.append(strSymbols[ranSym])

    for i in range(noNum):
        ranSym = random.randint(0,9)
        pwd.append(str(ranSym))

random.shuffle(pwd)  

outPwd = ''

for char in pwd:
    outPwd += char

print(outPwd)
             