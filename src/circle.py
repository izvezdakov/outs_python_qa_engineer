import math

from src.figure import Figure


class Circle(Figure):

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError
        self.radius = radius

    @property
    def name(self):
        return 'Circle'

    def perimeter(self) -> float:
        return self.radius * 2 * math.pi

    def area(self) -> float:
        return self.radius ** 2 * math.pi
