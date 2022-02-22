import math


class circle():
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius**2)

    def __str__(self):
        return f'Radius is {self.radius}'

    def __repr__(self):
        return f'Circle(radius={self.radius})'

    def __add__(self, other_circle):
        self.radius += other_circle.radius
        return self.radius

    def __gt__(self, other_circle):
        if self.radius > other_circle.radius:
            return 'Bigger'
        elif self.radius < other_circle.radius:
            return 'Smaller'
        else:
            return 'Equal!!!'
