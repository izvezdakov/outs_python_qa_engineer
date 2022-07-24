import pytest

from src.triangle import Triangle


def test_create_simple_triangle():
    tr = Triangle(3, 4, 5)
    assert tr


def test_area_is_calculated():
    tr = Triangle(3, 4, 5)
    h_p = (tr.second_side + tr.first_side + tr.third_side) / 2
    assert tr.area() == (h_p * (h_p - tr.first_side) * (h_p - tr.second_side) * (h_p - tr.third_side)) ** (1 / 2)


def test_perimeter_is_calculated():
    tr = Triangle(3, 4, 5)
    assert tr.perimeter() == 3 + 4 + 5


def test_name_is_correct():
    tr = Triangle(3, 4, 5)
    assert tr.name == 'Triangle'


@pytest.mark.parametrize('sides', [
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, -1, 1),
    (-1, 1, 1),
    (-1, 1, -1),
    (0, 1, -1),
    (1, 0, -1),
    (-1, -1, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0),
])
def test_impossible_create_triangle_with_negative_or_zero_sides(sides):
    with pytest.raises(ValueError):
        Triangle(*sides)


def test_impossible_create_incorrect_triangle():
    with pytest.raises(ValueError):
        Triangle(3, 4, 100500)
