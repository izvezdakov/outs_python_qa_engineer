from src.figure import Figure


class Triangle(Figure):

    def __init__(self, first_side: float, second_side: float, third_side: float):
        if first_side <= 0 or second_side <= 0 or third_side <= 0 or first_side + second_side <= third_side or \
                first_side + third_side <= second_side or second_side + third_side <= first_side:
            raise ValueError

        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    @property
    def name(self):
        return 'Triangle'

    def perimeter(self) -> float:
        return self.first_side + self.second_side + self.third_side

    def area(self) -> float:
        h_p = self.perimeter() / 2
        return (h_p * (h_p-self.first_side) * (h_p-self.second_side) * (h_p-self.third_side)) ** (1/2)
