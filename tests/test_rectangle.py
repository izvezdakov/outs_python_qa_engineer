import pytest

from src.rectangle import Rectangle


def test_create_simple_rectangle():
    rct = Rectangle(2, 4)
    assert rct


def test_area_is_calculated():
    rct = Rectangle(2, 4)
    assert rct.area() == rct.width * rct.length


def test_perimeter_is_calculated():
    rct = Rectangle(2, 4)
    assert rct.perimeter() == (rct.width + rct.length) * 2


def test_name_is_correct():
    rct = Rectangle(2, 4)
    assert rct.name == 'Rectangle'


@pytest.mark.parametrize('sides', [
    (1, -1),
    (0, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
])
def test_impossible_create_rectangle_with_negative_or_zero_sides(sides):
    with pytest.raises(ValueError):
        Rectangle(*sides)

