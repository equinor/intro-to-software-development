from geo_calculator.calculations import (
    find_average,
    gardners_equation,
    inverse_gardners_equation,
)
import pytest


def test_find_average_given_a_list_of_ints() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_average(numbers) == 3.5


def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
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


def test_inverse_gardners_equation_negative_density() -> None:
    density = -1000  # g/cm3
    with pytest.raises(ValueError) as e:
        inverse_gardners_equation(density)
