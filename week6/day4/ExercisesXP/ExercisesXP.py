# ---------------Exercises XP--------------

# Exercise 1 : Favorite Numbers:
from os import remove


my_fav_numbers = {4, 6, 8, 17, 22, 23}
new_numbers = (23, 24)
my_fav_numbers.add(new_numbers)
friend_fav_numbers = {2, 13, 25, 16}
our_fav_numbers = set.union(my_fav_numbers, friend_fav_numbers)
print(our_fav_numbers)


# Exercise 2: Tuple:
# Given a tuple which value is integers, is it possible to add more integers to the tuple?: NO.

# Exercise 3: Print A Range Of Numbers:

for num in range(1, 22):
    print(num, end=" ")


# Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?:
# INTEGER is a round number whereas FLOAT is a any number with a decimal after it 1.0, 0.0 ,200.0000 11.24 etc...

# Exercise 5: Shopping List:
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# 1.Remove “Banana” from the list.
basket.pop(0)
# 2.Remove “Blueberries” from the list.
basket.pop(-1)
# 3.Add “Kiwi” to the end of the list.
basket.append('Kiwi')
# 4.Add “Apples” to the beginning of the list.
basket.insert(0, "Apples")
# 5.Count how many apples are in the basket.
apple_amount = basket.count('Apples')
# 6.Empty the basket.
basket.clear()
# 7.Print(basket)
print(basket)


# Exercise 6 : Loop
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name:
while True:
    usr_nm = input('Please enter your name: ').lower()
    if usr_nm == 'ofir':
        print('Dope, your name is exactly like mine!!!')
        break

# Exercise 7
# Given a list, use a loop to print out every element which has an even index.
for num in range(1, 22):
    if not num % 2:
        print(num, end=" ")

# Exercise 8
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for num in range(1500, 2500):
    if (not num % 5) and (not num % 7):
        print(num, end=" ")

# Exercise 9: Favorite Fruits
# 1.Ask the user to input their favorite fruit(s) (one or several fruits). Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry":
fvrt_frt = input(
    "Please write down a list of all of your favorite fruits with a space between each one: ").lower()
# 2.Store the favorite fruit(s) in a list (convert the string of words into a list of words):
fvrt_frt_lst = fvrt_frt.split()
# 3.Now that we have a list of fruits, ask the user to input a name of any fruit.
name_frt = input(
    "Please write the name of any of the fruits you have listed down: ").lower()

if name_frt in fvrt_frt_lst:
    print("You chose one of your favorite fruits! Enjoy!")
if name_frt not in fvrt_frt_lst:
    print("You chose a new fruit. I hope you enjoy")


# Exercise 10: Who Ordered A Pizza ?:
# 1.Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
topping_list = []
while True:
    topping = input(
        'Please write a list of topping for your pizza, if you have completed write "quite": ')
    topping_list.append(topping)
    print("you’ll add that topping to their pizza")
# 2.As they enter each topping, print a message saying you’ll add that topping to their pizza.
    if topping != "quite":
        continue
    break
topping_list.pop(-1)
topping_str = ', '.join(map(str, topping_list))
# 3.Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
number_of_items = len(topping_list)
total = int((number_of_items * 2.5) + 10)
print("Your toppings are: " + topping_str +
      f' and your total price is: {total}')


# Exercise 11: Cinemax
""" 1. movie theater charges different ticket prices depending on a person’s age.if a person is under the age of 3, the ticket is free.if they are between 3 and 12, the ticket is $10.if they are over the age of 12, the ticket is $15.
2.Ask a family the age of each person who wants a ticket.
3. Store the total cost of all the family’s tickets and print it out."""
family_list = []
while True:
    ages_for_tickes = input(
        "Please indicate the age of each family member, when finished use 0 to quite: ")
    age = int(ages_for_tickes)
    family_list.append(int(ages_for_tickes))
    if ages_for_tickes != '0':
        continue
    break
family_list.pop(-1)

tickets_total = 0
for age in family_list:
    if age <= 3:
        tickets_total += 0
    elif age >= 3 or age <= 12:
        tickets_total += 10
    else:
        tickets_total += 15
print(f'the total tickets price is {tickets_total}')
"""4. A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie."""
restriction_list = []
while True:
    check_teens_age = input(
        "Please indicate the age of each teen, when finished use 0 to quite: ")
    check_teens_age_int = int(check_teens_age)
    restriction_list.append(check_teens_age_int)
    if check_teens_age != '0':
        continue
    break
restriction_list.pop(-1)
for teen_age in range(16, 22):
    if teen_age in restriction_list:
        restriction_list.remove(teen_age)
print(
    f' only teens in the age of {restriction_list} are allowed to watch the movie')

# Exercise 12 : Who Is Under 16?
"""1.Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
2. At the end, print the final list"""
names_list_age = []
while True:
    ages_in_list = input(
        'Please write the age of each person, to quite press q: ')
    names_list_age.append(ages_in_list)
    if ages_in_list != 'q':
        continue
    break
names_list_age.pop(-1)
int_map = map(int, names_list_age)
int_names_list_age = list(int_map)

for age in range(1, 17):
    if age in int_names_list_age:
        int_names_list_age.remove(age)
print(int_names_list_age)

# Exercise 13
# 1.Make a list called sandwich_orders and fill it with the names of various sandwiches .
sandwich_orders = ["Cheeseburger", "Tuna", "Mozarella", "Roastbeef"]
# 2.Then make an empty list called finished_sandwiches.
finished_sandwiches = []
# 3.As each sandwich is made, move it to the list of finished sandwiches.
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
# 4.After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
for completed in finished_sandwiches:
    print(f'I have made you a {completed} sandwich')


# Exercise 13
# 1.Make a list called sandwich_orders and fill it with the names of various sandwiches .
sandwich_orders = ["Cheeseburger", "Tuna", "Mozarella", "Roastbeef"]
# 2.Then make an empty list called finished_sandwiches.
finished_sandwiches = []
# 3.As each sandwich is made, move it to the list of finished sandwiches.
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
# 4.After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
for completed in finished_sandwiches:
    print(f'I have made you a {completed} sandwich')

# Exercise 14
# 1.Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
new_sandwitch = ["pastrami"] * 3
sandwich_orders.extend(new_sandwitch)
print(sandwich_orders)
# 2.Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
print('the deli has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# 3.Make sure no pastrami sandwiches end up in finished_sandwiches.
new_finished_sandwiches = []
for sandwich in sandwich_orders:
    new_finished_sandwiches.append(sandwich)
print(new_finished_sandwiches)
