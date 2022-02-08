# Exercises XP Gold


# Exercise 1: Birthday Look-Up
# 1.Create a variable called birthdays. Its value should be a dictionary.
# 2.Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday.
birthdays = {'Eitan': '2019/01/06', 'Fabiana': '1991/06/17',
             'Ehud': '1951/08/23', 'Ilana': '1951/08/23', 'Lital': '1985/04/08'}

# 3.Print a welcome message for the user.
print("Welcome")
print("You can look up the birthdays of the people in the list!")
print(birthdays)

# Ask the user to give you a person’s name and store the answer in a variable.
user_name_of_choice = input("Please indicate a name of a person you know: ")
# Get the birthday of the name provided by the user.
user_person_bd = input(
    "Please indicate the date of birth of the person you have chosen YYYY/MM/DD: ")
# Print out the birthday with a nicely-formatted message.
print(f'{user_name_of_choice} will have is birthday on the {user_person_bd}')

# Exercise 2: Birthdays Advanced
# 1.Before asking the user to input a person’s name print out all of the names in the dictionary.
# 2.If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)

birthdays = {'Eitan': '2019/01/06', 'Fabiana': '1991/06/17',
             'Ehud': '1951/08/23', 'Ilana': '1951/08/23', 'Lital': '1985/04/08'}

print("Welcome")
print("You can look up the birthdays of the people in the list!")
print(birthdays)

user_name_of_choice = input(
    "Please indicate a name of a person you know: ").capitalize()

if user_name_of_choice in birthdays:
    print(
        f'{user_name_of_choice} will have is birthday on the {birthdays[user_name_of_choice]}')
else:
    print(
        f"Sorry, we don’t have the birthday information for {user_name_of_choice} ")
