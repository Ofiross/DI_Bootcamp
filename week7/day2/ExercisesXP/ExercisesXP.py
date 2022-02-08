# Exercises XP #1

# Exercise 1 : What Are You Learning ?
# 1.Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
from cgitb import small
import random


def display_message():
    print("I am learning web development")


# 2.Call the function, and make sure the message displays correctly.
display_message()


# Exercise 2: What’s Your Favorite Book ?
# 1.Write a function called favorite_book() that accepts one parameter called title.
def favorite_book(title):
    # 2.The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
    print("One of my favorite books is " + title)


# 3.Call the function, make sure to include a book title as an argument when calling the function.
favorite_book("The Mamba mentality")


# Exercise 3 : Some Geography
# 1.Write a function called describe_city() that accepts the name of a city and its country as parameters.
def describe_city(city, country='Israel'):
    # 2.The function should print a simple sentence, such as “Reykjavik is in Iceland”.
    print(city + " is in " + country)


# 3.Give the country parameter a default value.
# 4.Call your function.
describe_city("Tel Aviv")


# Exercise 4 : Random
""" Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display 
both numbers."""


def number_compare():
    while True:
        usr_number = int(input("Please pick a number from 1 - 100: "))
        if usr_number < 1 or usr_number > 100:
            continue
        break
    random_num = random.randint(1, 100)
    if usr_number == random_num:
        print("Good you have guessed the number")
    else:
        print(f"You have guessed wrong, the PC number is {random_num}")


number_compare()


# Exercise 5 : Let’s Create Some Personalized Shirts !
# 1.Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
def make_shirt(size, text):
    # 2.The function should print a sentence summarizing the size of the shirt and the message printed on it
    print(
        f'The size of the shirt is {size} and the text asked to be printed on the shirt is: "{text}"')


# 3.Call the function make_shirt() using positional arguments to make a shirt.
make_shirt('XL', 'Hello World')

# 4.Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# 5.Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


def make_shirt(size='large', text='I love Python'):
    print(
        f'The size of the shirt is {size} and the text asked to be printed on the shirt is: "{text}"')


make_shirt()


def make_shirt(size='medium', text='I love Python'):
    print(
        f'The size of the shirt is {size} and the text asked to be printed on the shirt is: "{text}"')


make_shirt()


def make_shirt(size, text='I also love JavaScript'):
    print(
        f'The size of the shirt is {size} and the text asked to be printed on the shirt is: "{text}"')


make_shirt(small)

# 6.Bonus: Call the function make_shirt() using keyword arguments.


def make_shirt(size='XXL', text='Hello'):
    print(
        f'The size of the shirt is {size} and the text asked to be printed on the shirt is: "{text}"')


make_shirt()


# Exercise 6 : Magicians …
# 1.Make a list of magician’s names.
mag_nms = ['David Copperfield', 'Doug Henning',
           'Mark Wilson', 'Harry Anderson']

# 2.Pass the list to a function called show_magicians(), which prints the name of each magician in the list


def show_magicians(mag_nms):
    for name in mag_nms:
        print(name)


def make_great(mag_nms):
    # New empty list to add names into
    great_mag = []
    # add the great to each name
    while mag_nms:
        name_of_mag = mag_nms.pop()
        mag = name_of_mag + ' the Great'
        great_mag.append(mag)

    # after eliminating each magician we add them back with the great word into the first list.
    for mag in great_mag:
        mag_nms.append(mag)


make_great(mag_nms)
show_magicians(mag_nms)
