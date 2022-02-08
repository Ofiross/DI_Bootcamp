# Exercises XP Gold

#   Exercise 1: Temperature Advice
import random


def get_random_temp():
    """
    Info: function that generate random number between -10 and 40.
    """
    return(random.randint(-10, 40))

# 2.Create a function called main()
# 3.Let’s add more functionality to the main() function


def main():
    """
    Info: the function generate a message to the user base on the temperature.
    """
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print(f"Brrr, that’s freezing! Wear some extra layers today!")
    elif 0 < temp < 16:
        print(f"Quite chilly! Don’t forget your coat!")
    elif 16 < temp < 23:
        print("The weather is fine today, some light jacket will work just fine.")
    elif 24 < temp < 32:
        print("It is summer time weather outside, enjoy it!")
    elif 32 < temp < 400:
        print("It is hot as hell outside, drink a lot and don't stay for too long under the sun!")


main()
