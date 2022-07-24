from src.figure import Figure


class Square(Figure):

    def __init__(self, side: float):
        if side <= 0:
            raise ValueError
        self.side = side

    @property
    def name(self):
        return 'Square'

    def perimeter(self) -> float:
        return self.side * 4

    def area(self) -> float:
        return self.side ** 2
