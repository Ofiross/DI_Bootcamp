import random
import re
import string

# Exercise 1
string_to_check = "'k5k3q2g5z6x9bn'"
match = re.findall('[0-9]', string_to_check)
if (match):
    match_result = ' '.join([str(elem) for elem in match])
    print(match_result)
else:
    print("String not found!")


# Exercise 2
def state_your_full_name():
    charRe = re.compile(r'[^a-zA-Z]')
    user_input = ('Please state your full name: ')
    string = charRe.search(user_input)
    if string:
        return string


# Exercise 3


# characters to generate password from


# declaring variables
password_length = 0
password = ''

# starting executing


def password_generator():
    """Password Generator"""
    print(f"{'-'*20}\nPASSWORD GENERATOR\n{'-'*20}")

    password_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                      'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    password_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    password_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_symb = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_length = 0

    while password_length is not int:
        try:
            password_length = int(
                input('Choose password length with a minimum of 6 maximum 30: '))
            if password_length < 6 or password_length > 30:
                raise ValueError
            break
        except ValueError:
            print('Length too short!!!')
            print('Please enter a valid number: ')

    password = ""
    for i in range(password_length - 7):
        password += random.choice(password_lower)
    password += random.choice(password_num)
    password += random.choice(password_upper)
    password += random.choice(password_symb)
    password += random.choice(password_num)
    password += random.choice(password_upper)
    password += random.choice(password_symb)
    password += random.choice(password_lower)

    if password_length == 6:
        six_password = password[:2] + password[3:]
        li = list(six_password.split(" "))
        random.shuffle(li)
        final_psw = ' '.join([str(elem) for elem in li])
        print(f"Your generated password is: \n{final_psw}")

    else:
        li = list(password.split(" "))
        random.shuffle(li)
        final_psw = ' '.join([str(elem) for elem in li])
        print(f"Your generated password is: \n{final_psw}")


password_generator()
