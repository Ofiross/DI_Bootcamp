# Exercise Xp

# Exercise 1
import print_something
from print_something import Print
from print_something import Print as fn
import print_something as mn
import random
import string

# Exercise 2


def check_guess():
    print('Guess the PC number.')
    while True:
        try:
            user_guess = int(input('Choose number from 1 - 100: '))
            if user_guess < 1 or user_guess > 100:
                raise ValueError
            break
        except ValueError:
            print("That's not a valid option!")
            print("You can choose only number from 1 - 100")
    pc_num = (random.randint(1, 100))
    if user_guess == pc_num:
        print(
            f'Great you have guessed the number:\nYour number --> {user_guess}\nPC number --> {pc_num}')
    else:
        print(
            f'Bad guess!!!\nYour number --> {user_guess}\nPC number --> {pc_num}')


check_guess()


# Exercise 3
def rand_str():
    letters = string.ascii_uppercase
    result = ''.join(random.choice(letters) for i in range(5))
    print(f"A random srting in the length of 5:\n{result}")


rand_str()
