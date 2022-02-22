# Exercises XP - OOP
class Human:
    def __init__(self, name, age=1, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building
        building.inhabitants.append(self)


class Building:
    inhabitants = []

    def __init__(self, address):
        self.address = address

    def average_age(self):
        ave_age = sum([int(n) for n in self.inhabitants if n])
        return ave_age


class City:
    buildings = []

    def __init__(self, name):
        self.name = name

    def construct(self, address):
        self.buildings.append(Building(address))


tel_aviv = City('Tel Aviv')
tel_aviv.construct('Dizinkof 42')
ofir = Human('Ofir', 32)
fabiana = Human('Fabiana', 30)
