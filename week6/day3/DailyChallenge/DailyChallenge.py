# Daily Challenge: Build Up A String


while True:
    user_inpt = input('Please enter a sentence which is 10 letters long: ')
    lengthOfInput = len(user_inpt)
    if lengthOfInput < 10:
        print("string not long enough")
    elif lengthOfInput > 10:
        print("string too long")
    else:
        print(user_inpt[0] + user_inpt[-1])
        break

ltr = ''
for char in user_inpt:
   ltr += char
   print (ltr)

import random

newUsrInpt = ''.join(random.sample(user_inpt, len(user_inpt)))
print('A new random string is:' + newUsrInpt)