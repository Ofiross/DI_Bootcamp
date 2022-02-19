# DAILY CHALLENGE.

# Part 1 : Quizz :

from random import shuffle
print("""
Answer the following questions
-------------------------------
What is a class? a class is a template, blueprint, which contain all of the details and functionalety later on for the objects.
------------------------------------------------------------------------------------------------------------------------------------------
What is an instance? an instance is that object which will make use of the data created inside the class.
------------------------------------------------------------------------------------------------------------------------------------------
What is encapsulation? encapsulation means storing data in single object, packing data and functions that is working on that object
------------------------------------------------------------------------------------------------------------------------------------------
What is abstraction? abstraction is hiding unnessessary information from the user and storing that information inside the code solely
------------------------------------------------------------------------------------------------------------------------------------------
What is inheritance? inheritance in python is making use the data structure from one class inside another without the need to create all the structure or methods again.
------------------------------------------------------------------------------------------------------------------------------------------
What is multiple inheritance? like the name is stating it is the same as inheritance just that in this case the inheritance of the function is from two or more classes.
------------------------------------------------------------------------------------------------------------------------------------------
What is polymorphism? the translte mean "having many form", in the case of python or any other programming language the meaning is one function name, or method, is being used for diffrent types in diffrent scenarios.
------------------------------------------------------------------------------------------------------------------------------------------
What is method resolution order or MRO? a concept of inheritence which creates hierarchy and the order in which the inheritece will move from one method to another.
------------------------------------------------------------------------------------------------------------------------------------------
""")


# Part 2: Create A Deck Of Cards Class.

class Card:
    global cards_suit, cards_value
    cards_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    cards_value = ['A', '2', '3', '4', '5',
                   '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        pass


class Deck:
    def __init__(self):
        Card.__init__(self)
        self.cards = []
        for s in cards_suit:
            for n in cards_value:
                self.cards.append((s) + " " + "of" + " " + n)

    def shuffle(self):
        if len(self.cards) < 52:
            print("Sorry cannot shuffle less than 52 cards.")
        else:
            shuffle(self.cards)
            return self.cards

    def deal(self):
        card_removed = self.cards.pop()
        print(f"Card removed is: {card_removed}")


game_deck = Deck()
game_cards = game_deck.cards
print(f"Game cards are: {game_cards}")
game_deck.shuffle()
game_deck.deal()
