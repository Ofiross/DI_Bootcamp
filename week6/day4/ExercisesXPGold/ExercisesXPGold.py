# Exercises XP Gold

# Exercise 1 : Concatenate Lists
# 1. Write code that concatenates two lists together without using the + sign.
""" list1 = [1, 2, 3, 4, 5]
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
 """

# Exercise 5 : Words And Letters
# 1.Ask a user for 7 words, store them in a list named words.
words_length = 0
while words_length < 7:
    usr_words = input('Please write down 7 words: ')
    words = list(usr_words.split(" "))
    words_length += len(words)

while len(char) < 1 or len(char > 1):
    char = input("Please indicate a single character of your choice: ")
