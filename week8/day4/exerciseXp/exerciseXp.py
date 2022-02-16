# Exercises XP


# Exercises 1: Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1 = Bengal
cat2 = Chartreux
cat3 = Persian

my_cats = [cat1('Max', 4), cat2('Garfield', 8), cat3('Sam', 5)]

my_pets = Pets(my_cats)
my_pets.walk()

print('\n')


# Exercise 2 : Dogs
class Dogs:
    def __init__(self, dogs):
        self.dogs = dogs

    def fight(self):
        for dog in self.dogs:
            print(dog.fight())


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking.'

    def run_speed(self):
        return(int(self.weight/self.age)*10)

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            return f'The winner is {self.name}'
        else:
            return f'The winner is {other_dog.name}'


dog1 = Dog('Rex', 5, 20)
dog2 = Dog('Max', 4, 30)
dog3 = Dog('Marcus', 8, 23)


my_dogs = Pets(my_cats)

dog1.run_speed()
dog2.run_speed()
dog3.run_speed()
print(f"Between {dog1.name} and {dog2.name} {dog1.fight(dog2)}")
print(f"Between {dog1.name} and {dog3.name} {dog1.fight(dog3)}")
print(f"Between {dog2.name} and {dog3.name} {dog2.fight(dog3)}")
