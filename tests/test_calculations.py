import pytest

from geo_calculator.calculations import (
    find_average,
    gardners_equation,
    inverse_gardners_equation,
)


def test_find_average_given_a_list_of_ints() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_average(numbers) == 3.5


def test_gardners_equation() -> None:
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    assert gardners_equation(velocity) == pytest.approx(expected_density)


def test_inverse_gardners_equation() -> None:
    density = 2.0730949  # g/cm3
    expected_velocity = 2000  # m/s

    assert inverse_gardners_equation(density) == pytest.approx(expected_velocity)

    assert inverse_gardners_equation(
        gardners_equation(expected_velocity)
    ) == pytest.approx(expected_velocity)

    assert gardners_equation(inverse_gardners_equation(density)) == pytest.approx(
        density
    )


def test_gardners_equation_negative_velocity() -> None:
    velocity = -1000  # m/s
    with pytest.raises(ValueError) as e:
        gardners_equation(velocity)


def test_inverse_gardners_equation_negative_velocity() -> None:
    density = -1000  # g/cm3
    with pytest.raises(ValueError) as e:
        inverse_gardners_equation(density)
