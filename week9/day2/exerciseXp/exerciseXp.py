# Exercises XP


# Exercise 1 : Built-In Functions
""" print('\n')
print('int doc'.upper())
print('---------------')
print(int.__doc__)
print('*********************************************************************************************************************')
print('\n')
print('abs doc'.upper())
print('---------------')
print(abs.__doc__)
print('*********************************************************************************************************************')
print('\n')
print('input doc'.upper())
print('---------------')
print(input.__doc__) """


# Exercise 2: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return(f"'{self.amount} {self.currency}{'s' if self.amount > 1 else ''}'")

    def __repr__(self):
        return(f"'{self.amount} {self.currency}{'s' if self.amount > 1 else ''}'")

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if type(other) == (int):
            return Currency(self.currency, self.amount + other)
        elif self.currency == other.currency:
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError(
                "Cannot add between Currency type <dollar> and <shekel>")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
c1 + c3
