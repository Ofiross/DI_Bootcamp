# Exercises XP

# Exercise 1 : Convert Lists Into Dictionaries
# 1.Convert the two following lists, into dictionaries.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Using dict and zip to convert the two lists to a dictionary, the dict change the list to a dictionary, the zip is taking first value from each list and making theme a pair, then the second value from each list and etc....
list_to_dict = dict(zip(keys, values))
print(list_to_dict)


# Exercise 2 : Cinemax #2
# “Continuation of Exercise Cinemax from Week4Day2 XP”
""" 1.A movie theater charges different ticket prices depending on a person’s age.
• if a person is under the age of 3, the ticket is free.
• if they are between 3 and 12, the ticket is $10.
• if they are over the age of 12, the ticket is $15."""
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# 3.How much does each family member have to pay ?
# 4.Print out the family’s total cost for the movies.
tickets_total = 0
for name, age in family.items():
    if age <= 3:
        price = 0
        tickets_total += 0
        print(f'{name} will pay {price}')
    elif age > 12:
        price = 15
        tickets_total += 15
        print(f'{name} will pay {price}')
    else:
        price = 10
        tickets_total += 10
        print(f'{name} will pay {price}')
print(f'The whole family tickets price is: {tickets_total}')

# 5.Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# Creating empty lists to add name and age into with every loop:
names = []
ages = []
# Creating a loop to ask the user to add new family members name and age:
while True:
    # check the input is only A-Z
    while True:
        usr_fmly_nms = input("Please indicate the person name: ")
        names.append(usr_fmly_nms)
        if usr_fmly_nms.isalpha():
            break
    # check the age is only Number
    while True:
        usr_fmly_ags = int(input("Please indicate the person age: "))
        ages.append(usr_fmly_ags)
        if type(usr_fmly_ags) == int:
            break
    # ask if the user wants to add a new family member
    while True:
        another_person = input(
            "whould you like to add another person? y for yes n for no: ").lower()
        if another_person.isalpha():
            break
    if another_person == 'n':
        break
# making a dictionary from the names and age lists
usr_family = dict(zip(names, ages))
# conditions for know how much wiil a ticket cost to each person and printing each one price and the total price by creating a variable which is equals 0 and add into it the price of every person
tickets_total = 0
for name, age in usr_family.items():
    if age <= 3:
        price = 0
        tickets_total += 0
        print(f'{name} will pay {price}')
    elif age > 12:
        price = 15
        tickets_total += 15
        print(f'{name} will pay {price}')
    else:
        price = 10
        tickets_total += 10
        print(f'{name} will pay {price}')
print(f'The whole family tickets price is: {tickets_total}')


# Exercise 3: Zara
# 1.Here is some information about a brand.
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
brand = {'name': 'Zara', 'creation_date': '1975', 'creator_name': 'Amancio Ortega Gaona', 'type_of_clothes': ['men', 'women', 'children', 'home'], 'international_competitors': [
    'Gap', 'H&M', 'Benetton'], 'number_stores': '7000', 'major_color': {'France': 'blue', 'Spain': 'red', 'US': ['pink', 'green']}}
# 3.Change the number of stores to 2.
brand['number_stores'] = 2
# 4.Print a sentence that explains who Zaras clients are
zara_clients1 = brand['type_of_clothes'][0]
zara_clients2 = brand['type_of_clothes'][1]
zara_clients3 = brand['type_of_clothes'][2]
zara_clients4 = brand['type_of_clothes'][3]
print(
    f'Zaras clients are {zara_clients1}, {zara_clients2}, {zara_clients3}, and they also sell {zara_clients4} materials.')
# 5.Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
# 6.Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
brand['international_competitors'].append("Desigual")
# 7.Delete the information about the date of creation.
del(brand['creation_date'])
# 8.Print the last international competitor
print(brand['international_competitors'][-1])
# 9.Print the major clothes colors in the US.
print(brand['major_color']['US'][0], brand['major_color']['US'][1])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print("Length of dictionary:", len(brand))
# 11. Print the keys of the dictionary.
for keys in brand:
    print(keys)
# 12. Create another dictionary called more_on_zara with the following details:
more_on_zara = {'creation_date': '1975', 'number_stores': '10 000'}
# 13. Use a method to add the information from the dictionary more_on_zara
# 13. Use a method to add the information from the dictionary more_on_zara
brand.update(more_on_zara)
# 14. Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])


# Exercise 4 : Disney Characters
# Use this list :
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# 1. Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
dictOfWords = {users[i]: i for i in range(0, len(users))}
print(dictOfWords)
# 2.{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# 2.Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
dictOfWords = {i: users[i] for i in range(0, len(users))}
print(dictOfWords)
# 3.{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# 3.Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
users.sort()
dictOfWords = {users[i]: i for i in range(0, len(users))}
print(dictOfWords)
