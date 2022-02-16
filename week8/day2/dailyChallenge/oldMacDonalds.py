
class Farm():
    def __init__(self, owners_name):
        self.name = owners_name
        self.animals = {}
        print(f"{self.name}'s farm")

    def add_animal(self, animal_name, amount=1):
        if animal_name in self.animals:
            self.animals[animal_name] += amount
        else:
            self.animals[animal_name] = amount

    def get_info(self):
        for k, v in self.animals.items():
            print(f'{k} : {v}')
        return("\tE-I-E-I-0!")


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
