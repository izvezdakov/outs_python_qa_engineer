import math

import pytest

from src.circle import Circle


def test_create_simple_circle():
    cir = Circle(9)
    assert cir


def test_area_is_calculated():
    cir = Circle(9)
    assert cir.area() == cir.radius ** 2 * math.pi


def test_perimeter_is_calculated():
    cir = Circle(9)
    assert cir.perimeter() == 2 * math.pi * cir.radius


def test_name_is_correct():
    cir = Circle(9)
    assert cir.name == 'Circle'


@pytest.mark.parametrize('rad', [-1, 0])
def test_impossible_create_circle_with_negative_or_zero_rad(rad):
    with pytest.raises(ValueError):
        Circle(rad)

