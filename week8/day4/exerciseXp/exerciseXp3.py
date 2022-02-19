# Exercise 3 : Dogs Domesticated
from random import randint
from exerciseXp import Dog


class PetDog():
    def __init__(self, trained=False):
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f'{args} all play together!!!')

    def do_a_trick(self):
        possibilities = ['does a barrel roll',
                         'stands on his back legs', 'shakes your hand', 'plays dead']
        if self.trained == True:
            print(possibilities[randint(0, 3)])
