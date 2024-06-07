import pytest

from geo_calculator.calculations import (
    find_average,
    gardners_equation,
    inverse_gardners_equation,
)


def test_find_average_given_a_list_of_ints():
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_average(numbers) == 3.5


def test_find_average_fails_on_empty_list():
    numbers = []
    with pytest.raises(ZeroDivisionError) as e:
        find_average(numbers)


def test_gardners_equation():
    velocity = 2000  # m/s (up to 3500) (water is 1486, lowest possible, given no gas)
    density = 2000  # kg/m2 [2000-2600]

    assert gardners_equation(velocity) == density
    assert inverse_gardners_equation(density) == velocity

    assert inverse_gardners_equation(gardners_equation(velocity)) == velocity
    assert gardners_equation(inverse_gardners_equation(density)) == density


def test_gardners_equation_negative_velocity():
    velocity = -10  # m/s
    with pytest.raises(ValueError) as e:
        gardners_equation(velocity)
