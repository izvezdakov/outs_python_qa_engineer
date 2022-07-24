import pytest

from src.square import Square


def test_create_simple_square():
    sq = Square(3)
    assert sq


def test_area_is_calculated():
    sq = Square(3)
    assert sq.area() == sq.side ** 2


def test_perimeter_is_calculated():
    sq = Square(3)
    assert sq.perimeter() == 4 * sq.side


def test_name_is_correct():
    sq = Square(3)
    assert sq.name == 'Square'


@pytest.mark.parametrize('side', [0, -1])
def test_impossible_create_square_with_negative_or_zero_side(side):
    with pytest.raises(ValueError):
        Square(side)

