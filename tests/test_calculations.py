import pytest

from geo_calculator.calculations import (
    find_average,
    gardners_equation,
    inverse_gardners_equation,
)


def test_find_average_given_a_list_of_ints():
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_average(numbers) == 3.5


def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2073.0949  # kg/m2

    assert gardners_equation(velocity) == pytest.approx(expected_density)


def test_inverse_gardners_equation():
    density = 2073.0949  # kg/m2
    expected_velocity = 2000  # m/s

    assert inverse_gardners_equation(density) == pytest.approx(expected_velocity)

    assert inverse_gardners_equation(
        gardners_equation(expected_velocity)
    ) == pytest.approx(expected_velocity)

    assert gardners_equation(inverse_gardners_equation(density)) == pytest.approx(
        density
    )


def test_gardners_equation_negative_velocity():
    velocity = -1000  # m/s
    with pytest.raises(ValueError) as e:
        gardners_equation(velocity)


def test_inverse_gardners_equation_negative_velocity():
    density = -1000  # kg/m3
    with pytest.raises(ValueError) as e:
        inverse_gardners_equation(density)
