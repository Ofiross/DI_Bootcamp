# Exercises XP Gold

# Exercise 1 : Concatenate Lists
# 1. Write code that concatenates two lists together without using the + sign.
import random
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list1.extend(list2)
print(list1)


# Exercise 2: Greatest Number
# 1.Ask the user for 3 numbers and print the greatest number.
length = 0
num_lst = []
while length < 3:
    length += len(num_lst)
    usr_inpt = int(input(
        "Please choose three numbers and after you wrote each one click enter to add it to a list: "))
    num_lst.append(usr_inpt)
greatest_num = max(num_lst)
print(greatest_num)

# Exercise 3 : The Alphabet
# 1. Create a string of all the letters in the alphabet
# 2. Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for letter in alphabet:
    if (letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
        print('The letter ' + letter + ' is a vowel!')
    else:
        print('The letter ' + letter + ' is not a vowel!')

# Exercise 4 :
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# 1.Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
usr_name = input("What is your name?: ")
if usr_name in names:
    first_occ = names.index(usr_name)
print(f'The index of the name in the names list is: {first_occ}')


# Exercise 5 : Words And Letters
# 1.Ask a user for 7 words, store them in a list named words.
words_length = 0
while words_length < 7 or words_length > 7:
    words_length = 0
    usr_words = input('Please write down 7 words not less and not more: ')
    words = list(usr_words.split(" "))
    words_length += len(words)
# 2.Ask the user for a single character, store it in a variable called letter.
char = ''
while len(char) > 1 or len(char) < 1:
    char += input("Please indicate a single character of your choice: ")
# 3.Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
for i in words:
    index = i.find(char)
    if char in i:
        print(index)
# 4.If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
    elif char not in i:
        print(f'Sorry cannot find your letter in {i}.')

# Exercise 6 :
# 1.Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
one_to_million = []
for num in range(1000001):
    one_to_million.append(num)
print(min(one_to_million))
print(max(one_to_million))
print(sum(one_to_million))

# Exercise 7 :
# 1.Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98
acceptables = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',']
user_numbers = ''
while True:
    user_numbers = input("Please write a list of number seperated by comma: ")
    if any(inpt not in acceptables for inpt in user_numbers):
        continue
    break
list_of_nums = list(user_numbers.split(","))
print(list_of_nums)
tuple_of_nums = tuple(list_of_nums)
print(tuple_of_nums)

# Exercise 8 : Random Number
# 1.sk the user to input a number from 1 to 9 (including).
game_on = 'y'
total_wins = 0
total_losts = 0
while game_on == 'y':
    while True:
        usr_choice = int(
            input('Please choose a number from 1-9 and hit enter: '))
        if usr_choice > 9 or usr_choice < 1:
            continue
        break
# 2.Get a random number between 1 and 9. Hint: random module.
    random_number = random.randint(0, 10)
# 3.If the user guesses the correct number print a message that says Winner.
    if usr_choice == random_number:
        total_wins += 1
        print('You guessed the right number, Winner!!!')

    else:
        total_losts += 1
        print(
            f'You didnt got the number, PC choose {random_number}, Better luck next time')
    # Bonus: use a loop that allows the user to keep guessing until they want to quit.
    game_on = input(
        'Would you like to have another try? y for yes n for no and hit enter: ')
# Bonus 2: on exiting the loop tally up and display total games won and lost.
print(f'You got {total_wins} wins.')
print(f'You have lost {total_losts} times')
