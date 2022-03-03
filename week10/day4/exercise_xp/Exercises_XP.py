import random
# Exercises XP

# Exercise 1


def get_words_from_file(file):
    with open(file, 'r') as f:
        list_of_lists = [f.read().replace("\n", ", ")]
        return list_of_lists


def get_random_sentence(lst):
    word_list = []
    while True:
        try:
            length = int(input(
                'Please indicate number between 2 and 20, for the amount of words you would like your sentence to include: '))
            if length < 2 or length > 20:
                raise ValueError
            break
        except ValueError:
            print("That's not a valid option!")

    for i in range(length):
        word_list.append(random.choice(lst))

    sentence = ' '.join([str(elem) for elem in word_list])
    print(sentence)


def main():
    print("The program is taking a number between 2 - 20 and it is creating a random sentence base on the amount of the words the user indicates.")

    list_of_word = get_words_from_file('sowpods.txt')
    get_random_sentence(list_of_word)


if __name__ == "__main__":
    main()
