# Exercises XP+


# Exercise 1 : Family
print('\n')


class Family:

    members = [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
    ]

    last_name = ""

    @classmethod
    def born(cls, **kwargs):
        cls.name = kwargs.get('name', "")
        kwargs.setdefault('age', 0)
        cls.gender = kwargs.get('gender', 'x')
        kwargs.setdefault('is_child', True)
        cls.members.append(kwargs)
        for name_info in cls.members:
            if name_info['age'] < 1:
                print(f"welcome to the family little {name_info['name']}")

    def is_18(cls, name):
        dict_of_member = {}
        for i in cls.members:
            if i['name'] == name:
                dict_of_member = i
                if dict_of_member['age'] > 18:
                    return True
                else:
                    return False

    def family_info(cls):
        for info in cls.members:
            print(info)


some = Family()
some.born(name="Carl", gender='male')
print(some.members)
print(some.is_18('Carl'))


# Exercise 2 : TheIncredibles Family

print('\n')


class TheIncredibles(Family):

    members = []
    last_name = "Parr"

    @classmethod
    def born_with_powers(cls, **kwargs):
        cls.name = kwargs.get('name', "")
        kwargs.setdefault('age', 0)
        cls.gender = kwargs.get('gender', 'x')
        kwargs.setdefault('is_child', True)
        cls.power = kwargs.get('power', "p")
        cls.incredible_name = kwargs.get('incredible_name', "n")
        cls.members.append(kwargs)
        for name_info in cls.members:
            if name_info['age'] <= 1:
                print(f"welcome to the family little {name_info['name']}")
                print('\n')

    def use_power(cls):
        for name_info in cls.members:
            if name_info['age'] > 18:
                print(f"{name_info['power']}")
            else:
                raise ValueError("Under 18, cant use powers!")

    @classmethod
    def incredible_presentation(cls):
        for name_info in cls.members:
            print(
                f"My super hero name is: {name_info['incredible_name']} and my powers are: {name_info['power']}")


bob = TheIncredibles()
bob.born_with_powers(name='Robert', age=40, gender='male', is_child=False, power='Superhuman strength',
                     incredible_name='Mr. Incredible')

helen = TheIncredibles()
helen.born_with_powers(name='Helen', age=32, gender='female', is_child=False, power='Superhuman Elasticity',
                       incredible_name='Elastigirl')


violet = TheIncredibles()
violet.born_with_powers(name='Violet', age=14, gender='female', is_child=True, power='Invisibility',
                        incredible_name='Vi')

dash = TheIncredibles()
dash.born_with_powers(name='Dashiell Rober', age=10, gender='male', is_child=True, power='Super speed',
                      incredible_name='Dash')

jack = TheIncredibles()
jack.born_with_powers(name='John Jackson', age=1, gender='male', is_child=True, power='Unknown Power',
                      incredible_name='jack')


TheIncredibles.incredible_presentation()
