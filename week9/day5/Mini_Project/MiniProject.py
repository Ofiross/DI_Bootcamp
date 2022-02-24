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
        self.family.append(person)

    def get_family_info(self):
        for i, human in enumerate(self.family):
            print(i+1, '->', human.name)


class Queue:

    def __init__(self, humans=None):
        if not humans:
            self.humans = []

    def add_person(self, person):
        if person.prioritary or person.age > 60:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        return ([index for index, name in enumerate(self.humans) if name == person])

    def swap(self, person1, person2):
        first_person_index = self.humans.index(person1)
        second_person_index = self.humans.index(person2)
        self.humans.append(self.humans.pop(first_person_index))
        self.humans.insert(first_person_index,
                           self.humans.pop(second_person_index))
        self.humans.insert(second_person_index, self.humans.pop())

    def get_next(self):
        if len(self.humans) > 0:
            return self.humans.pop(0)
        else:
            print('No one more in the list.')
            return None

    def get_next_blood_type(self, blood_type):
        if len(self.humans) > 0:
            for person in self.humans:
                if person.blood_type == blood_type:
                    return self.humans.pop(self.humans(person))
        else:
            return None

    def sort_by_age(self):
        self.humans.sort(reverse=True, key=lambda person: [person.age])

    def get_list_info(self):
        for i, human in enumerate(self.humans):
            print(i+1, '->', human.name)

    def rearrange_queue(self):
        if len(self.humans) < 3:
            return
        for i in range(1, len(self.humans)):
            if self.humans[i].family == self.humans[i]:
                self.humans.sort(key=lambda person: [person.name])
