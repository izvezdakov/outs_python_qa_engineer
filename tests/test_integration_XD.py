import math


def test_circle_can_add_area_circle(circle_with_radius_one):
    assert circle_with_radius_one.add_area(circle_with_radius_one) == 2 * math.pi


def test_circle_can_add_area_square(circle_with_radius_one, square_with_side_one):
    assert circle_with_radius_one.add_area(square_with_side_one) == math.pi + 1


def test_circle_can_add_area_rectangle(circle_with_radius_one, rectangle_with_sides_two_three):
    assert circle_with_radius_one.add_area(rectangle_with_sides_two_three) == math.pi + (2 * 3)


def test_circle_can_add_area_triangle(circle_with_radius_one, triangle_with_sides_one_two_three):
    assert circle_with_radius_one.add_area(triangle_with_sides_one_two_three) == math.pi + 6


def test_rectangle_can_add_area_circle(rectangle_with_sides_two_three, circle_with_radius_one):
    assert rectangle_with_sides_two_three.add_area(circle_with_radius_one) == (2 * 3) + math.pi


def test_rectangle_can_add_area_square(rectangle_with_sides_two_three, square_with_side_one):
    assert rectangle_with_sides_two_three.add_area(square_with_side_one) == (2 * 3) + 1


def test_rectangle_can_add_area_rectangle(rectangle_with_sides_two_three):
    assert rectangle_with_sides_two_three.add_area(rectangle_with_sides_two_three) == (2 * 3) + (2 * 3)


def test_rectangle_can_add_area_triangle(rectangle_with_sides_two_three, triangle_with_sides_one_two_three):
    assert rectangle_with_sides_two_three.add_area(triangle_with_sides_one_two_three) == (2 * 3) + 6


def test_square_can_add_area_circle(square_with_side_one, circle_with_radius_one):
    assert square_with_side_one.add_area(circle_with_radius_one) == 1 + math.pi


def test_square_can_add_area_square(square_with_side_one):
    assert square_with_side_one.add_area(square_with_side_one) == 1 + 1


def test_square_can_add_area_rectangle(square_with_side_one, rectangle_with_sides_two_three):
    assert square_with_side_one.add_area(rectangle_with_sides_two_three) == 1 + (2 * 3)


def test_square_can_add_area_triangle(square_with_side_one, triangle_with_sides_one_two_three):
    assert square_with_side_one.add_area(triangle_with_sides_one_two_three) == 1 + 6


def test_triangle_can_add_area_circle(triangle_with_sides_one_two_three, circle_with_radius_one):
    assert triangle_with_sides_one_two_three.add_area(circle_with_radius_one) == 6 + math.pi


def test_triangle_can_add_area_square(triangle_with_sides_one_two_three, square_with_side_one):
    assert triangle_with_sides_one_two_three.add_area(square_with_side_one) == 6 + 1


def test_triangle_can_add_area_rectangle(triangle_with_sides_one_two_three, rectangle_with_sides_two_three):
    assert triangle_with_sides_one_two_three.add_area(rectangle_with_sides_two_three) == 6 + (2 * 3)


def test_triangle_can_add_area_triangle(triangle_with_sides_one_two_three):
    assert triangle_with_sides_one_two_three.add_area(triangle_with_sides_one_two_three) == 6 + 6
