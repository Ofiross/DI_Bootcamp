# Exercises XP

# Exercise 1: Cats

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat_sam = Cat('Sam', 5)
cat_lukas = Cat('Lukas', 3)
cat_garfield = Cat('Garfield', 10)


def oldest_cat(cat1, cat2, cat3):
    cats_gruop = {cat1.name: cat1.age,
                  cat2.name: cat2.age, cat3.name: cat3.age}
    new_val = max(cats_gruop, key=lambda x: cats_gruop[x])
    oldest = cats_gruop.get(f'{new_val}')
    result = (f'{new_val} and he is {oldest}')
    return result


print(
    f'The oldest cat is {oldest_cat(cat_sam, cat_lukas, cat_garfield)} years old.')

print('\n')
# Exercise 2 : Dogs


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = (self.height * 2)
        print(f"{self.name} jumps {x}cm high!")

    def dogs_info(self):
        print(f"Dogs name is {self.name} and he is {self.height}cm tall.")


davids_dog = Dog('Rex', 50)
davids_dog.dogs_info()
davids_dog.bark()
davids_dog.jump()
print('\n')
sarahs_dog = Dog('Teacup', 20)
sarahs_dog.dogs_info()
sarahs_dog.bark()
sarahs_dog.jump()
print('\n')
if davids_dog.height > sarahs_dog.height:
    print(f'The bigger dog is {davids_dog.name}')
else:
    print(f'The bigger dog is {sarahs_dog.name}')

print('\n')
# Exercise 3 : Who’s The Song Producer?


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):

        str_commas_seperated = ','.join([str(items) for items in self.lyrics])
        line_break = str_commas_seperated.replace(',', '\n')
        print(line_break)


stairway = Song(["There's a lady who's sure", "all that glitters is gold",
                "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()

print('\n')
# Exercise 4 : Afternoon At The Zoo


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals_lst = []
        self.a_z_sorted = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals_lst:
            self.animals_lst.append(new_animal)

    def get_animals(self):
        for animal in self.animals_lst:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals_lst:
            self.animals_lst.remove(animal_sold)
        else:
            print("Sorry no such animal in the zoo!")

    def sort_animals(self):
        for animal in self.animals_lst:
            self.a_z_sorted.setdefault(animal[0].upper(), []).append(animal)

    def get_groups(self):
        for key, value in self.a_z_sorted.items():
            print(key, ':', value)


ramat_gan_safari = Zoo('Ramat Gan Safari')
ramat_gan_safari.add_animal('giraf')
ramat_gan_safari.add_animal('monkey')
ramat_gan_safari.add_animal('lion')
ramat_gan_safari.add_animal('mouse')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
