from datetime import date
from datetime import datetime
# Exercises XP #2

# Exercise 7: When Will I Retire ?########################################################################################################


def get_age(year, month, day):
    """
    Info: function that generate the age of a person base on his birth date.
    """
    birthday = datetime.strptime(f"{year}/{month}/{day}", "%Y/%m/%d")

    today = date.today()
    age = today.year - birthday.year - \
        ((today.month, today.day) < (birthday.month, birthday.day))

    return int(age)


def can_retire(gender, date_of_birth):
    """
    Info: function that check if a person can retire base on his gender and age (Men, 67 / Women, 62)
    """
    bd = date_of_birth.split("/", 2)
    age = get_age(f'{bd[0]}', f'{bd[1]}', f'{bd[2]}')
    if (age > 67) and (gender == 'male'):
        print("You can retire!")
        return True
    elif (age < 67) and (gender == 'male'):
        print("You cannot retire!")
        return False
    elif gender == 'female' and age > 62:
        print("You can retire!")
        return True
    elif gender == 'female' and age < 62:
        print("You cannot retire!")
        return False


can_retire('male', '1989/6/22')


# Exercise 8:#############################################################################################################################
# 1.Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
def calculate_num(num):
    """
    Info: a function that gent an integer from 1-9 and calculate the sum of it as follow x+xx+xxx+xxxx.
    """
    result = num + (num * 11) + (num * 111) + (num * 1111)
    print(result)


calculate_num(3)
