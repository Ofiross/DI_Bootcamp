# Mini-Project: Characters Game
class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other_char):
        other_char.life - self.attack


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print("I am a Warrior!")

    def meditate(self):
        self.life += 10
        self.attack - 2
        return f"My life {self.life} my attack{self.attack}"

    def animal_help(self):
        self.attack += 5
        return f"My attack{self.attack}"

    def fight(self, other_char):
        other_char.life - (0.75*self.life + 0.75*self.attack)
        return f" My life {self.life} my attack {self.attack} other life {other_char.life}"


class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print("I am a Druid!")

    def brawl(self, other_char):
        other_char.attack - (2*self.attack)
        self.attack += (0.5*other_char.attack)
        return f" My life {self.life} my attack {self.attack} other life {other_char.life}"

    def train(self):
        self.attack += 2
        self.life += 2
        return f"My life {self.life} my attack{self.attack}"

    def roar(self, other_char):
        other_char.attack - 3
        return f"Other attack {other_char.attack}"


class Stinger(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print("I am a Mage!")

    def curse(self, other_char):
        other_char.attack - 2
        return f"Other attack {other_char.attack}"

    def summon(self):
        self.attack += 3
        return f"My attack{self.attack}"

    def cast_spell(self, other_char):
        other_char.attack - (self.attack/self.life)
        return f"Other attack {other_char.attack}"


druid_1 = Druid('Ofir')

warrior_1 = Warrior('Eitan')

stinger_1 = Stinger('Renato')
