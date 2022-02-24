from typing import List, Set
# Vaccines


class Human:

    def __init__(self, id_number: str, name: str, age: int, prioritary: bool, blood_type: str):
        blood_types = ['a', 'A', 'b', 'B', 'ab', 'AB', 'o', 'O']
        if blood_type in blood_types:
            self.id_number = id_number
            self.name = name
            self.age = age
            self.prioritary = prioritary
            self.blood_type = blood_type
            self.family = []

    def add_family_member(self, person):
        self.family.add(person)
        person.family.add(self)


class Queue:
    def __init__(self, humans: List = []):
        self.humans = humans

    def add_person(self, person: Human):
        if person.age or person.prioritary > 60:
            self.humans.append(person)

    def find_in_queue(self, person):
        return ([index for index, name in enumerate(self.humans) if name == person])

    def swap(self, person1, person2):
        self.humans[self.find_in_queue(person1)], self.humans[self.find_in_queue(
            person2)] = self.humans[self.find_in_queue(person2)], self.humans[self.find_in_queue(person1)]

    def get_next(self):
        if not self.humans == None:
            next_one = next(self.humans)
            self.humans.pop(next_one)
            return next_one
        else:
            return None

    def get_next_blood_type(self, blood_type):
        if not self.humans == None:
            blood_position = ([index for index, blood in enumerate(
                self.humans) if blood == blood_type])
            self.humans.pop(blood_position)
            return blood_position
        else:
            return None

    def sort_by_age(self):
        for i in range(len(self.humans)):
            for j in range(i+1, len(self.humans)):
                if self.humans[i] < self.humans[j]:
                    self.humans[i], self.humans[j] = self.humans[j], self.humans[i]
        return(self.humans)

    def rearrange_queue(self):
        if len(self.humans) < 3:
            return
        for i in self.humans:
            if next(self.humans) in self.humans.family:
                self.humans.sort()
