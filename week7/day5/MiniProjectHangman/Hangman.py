# HangMan Game
import random


def generate_word():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
                 'interference', 'complete', 'share', 'credit card', 'rush', 'south', 'angry', 'elephant', 'pinch', 'fish', 'reach',
                 'ball', 'flick', 'football', 'giggle', 'hammer', 'truck', 'photographer',  'duck', 'airplane', 'dog', 'zoo', 'city', 'island']
    word = random.choice(wordslist)
    return word
############################################################################################################################


def guess():
    """
    Info: a function that asks the player to guess a letter.
    """
    while True:
        guess = input('Please choose a letter to guess the word: ').upper()
        if not guess.isalpha():
            print("Please insert only letters!")
            continue
        elif len(guess) != 1:
            print("Please insert only one letter every time!")
            continue
        elif guess in used_letters:
            print('You have already guessed that letter. Choose again.')
            continue

        return guess

############################################################################################################################


HANGMAN = (
    """
        X-----------X
        |           |
        |
        |
        |
        |
        |
        |
        X------------------
    """,
    """
        X-----------X
        |           |
        |           O
        |
        |
        |
        |
        |
        X------------------
    """,
    """
        X-----------X
        |           |
        |           O
        |           |
        |
        |
        |
        |
        X------------------
    """,
    """
        X-----------X
        |           |
        |           O
        |          /|
        |
        |
        |
        |
        X------------------
    """,
    """
        X-----------X
        |           |
        |           O
        |          /|\\
        |
        |
        |
        |
        X------------------
    """,
    """
        X-----------X
        |           |
        |           O
        |          /|\\
        |          /
        |
        |
        |
        X------------------
    """,
    """
        X-----------X
        |           |
        |           O
        |          /|\\
        |          / \\
        |
        |
        |
        X------------------
    """)

############################################################################################################################


def replay():
    """
    Info: a function that asks the players if they want to play again.
    """
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

############################################################################################################################


def play_or_not():
    return input(
        'Are you ready to play? Enter y for Yes or n No: ').lower() == 'y'


# GAME SCRIPT##############################################################.
while play_or_not():
    TURN_LIMIT = len(HANGMAN) - 1
    print(
        "This is the Hangman guessing game, you will need to guess the word by choosing the letters inside it.")
    print("You will need to guess the word before the man will be hanged!!!")

    word_to_guess = generate_word().upper()

    hidden_word = "_" * len(word_to_guess)

    turn_number = 0

    used_letters = []

    tries = 7

    print("Welcome to Hangman. Good luck!")

    while tries != 0 and hidden_word != word_to_guess:
        print(HANGMAN[turn_number])
        print(f"You have {tries} more chances!")
        print(f"You have already used those letters:, {used_letters}")
        print(f"You should guess this word: {hidden_word}")

        player_guess = guess()

        used_letters.append(player_guess)

        if player_guess in word_to_guess:
            print(f"Great guess, the letter {player_guess} is in the word!")

            # create a new so_far to include guess
            temporary_string = ""

            for i in range(len(word_to_guess)):
                if player_guess == word_to_guess[i]:
                    temporary_string += player_guess
                else:
                    temporary_string += hidden_word[i]
            hidden_word = temporary_string

        else:
            print(f"Sorry, {player_guess}, isn't in word")
            turn_number += 1
            tries = tries - 1

    if turn_number == 6:
        print(HANGMAN[turn_number])
        print("congratulations you have guessed the word!")

    else:
        print("You are out of guesses, see you next time!")

    print(f"The word was {word_to_guess}")

    if not replay():
        break
