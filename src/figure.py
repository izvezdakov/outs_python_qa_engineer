from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

    def add_area(self, figure) -> float:
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area() + figure.area()
