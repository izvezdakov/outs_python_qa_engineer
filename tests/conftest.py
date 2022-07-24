import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture(scope='module')
def square_with_side_one():
    yield Square(1)


@pytest.fixture(scope='module')
def triangle_with_sides_one_two_three():
    yield Triangle(3, 4, 5)


@pytest.fixture(scope='module')
def rectangle_with_sides_two_three():
    yield Rectangle(2, 3)


@pytest.fixture(scope='module')
def circle_with_radius_one():
    yield Circle(1)
