from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError
        self.length = length
        self.width = width

    @property
    def name(self):
        return 'Rectangle'

    def perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def area(self) -> float:
        return self.width * self.length
