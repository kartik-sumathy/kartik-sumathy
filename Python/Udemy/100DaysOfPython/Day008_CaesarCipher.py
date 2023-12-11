import math
import string

#Area Calculator
# def print_calc(height, width, coverage):
#     area = height*width
#     coverage = math.ceil(area/coverage)
#     return coverage

# th = int(input("Enter height"))
# tw = int(input("Enter Width"))

# noOfCans = print_calc(th,tw,5)

# print(noOfCans)

#-----------------

# #Prime Calculator
# def checkPrime(n):
#     prime = True
#     for i in range(2,n):
#         if n % i == 0:
#             prime = False
#     return prime

# print({checkPrime(int(input("Enter Number")))})

#---------------------

def caesar(input, shift, encrypt):

    shift = shift % 26

    if encrypt is False:
        shift = shift * -1
    
    output = ''
    input = input.lower()
    lower = list(string.ascii_lowercase)
        
    for i in range(len(input)):
        if input[i] in lower:
            textIndex = lower.index(input[i])
            shiftIndex = textIndex+shift
            # output += lower[shiftIndex]
            if shiftIndex<25:
                output += lower[shiftIndex]
            else:
                shiftIndex = shiftIndex - 26
                output += lower[shiftIndex]
        else:
            output += input[i]
            
    return output


# print('Welcome to Caesar')
# Direction = input('Type Encode to Encrypt and Decode to Decrypt:')

# if Direction in ['Encode','Decode']:
#     textToProcess = input("Enter the text to be processed:")
#     numberToShift = int(input("Enter the Number of characters to split"))
    
# else:
#     print('Not a Valid Option')



# def textEncrypt(input, shift):
#     encrypt = ''
#     input = input.lower()
#     lower = list(string.ascii_lowercase)
#     for i in range(len(input)):
#         textIndex = lower.index(input[i])
#         shiftIndex = textIndex+shift
#         if shiftIndex<25:
#             encrypt += lower[shiftIndex]
#         else:
#             shiftIndex = shiftIndex - 26
#             encrypt += lower[shiftIndex]
#     return encrypt

# def textDecrypt(input, shift):
    # decrypt = ''
    # input = input.lower()
    # lower = list(string.ascii_lowercase)
    # for i in range(len(input)):
    #     textIndex = lower.index(input[i])
    #     shiftIndex = textIndex-shift
    #     if shiftIndex<25:
    #         shiftIndex = shiftIndex
    #         decrypt += lower[shiftIndex]
    #     else:
    #         shiftIndex = shiftIndex - 26
    #         decrypt += lower[shiftIndex]
    # return decrypt


EncryptedText =  caesar('zzz',50, True)

DecryptedText = caesar(EncryptedText,50, False)

print(EncryptedText)

print(DecryptedText)



