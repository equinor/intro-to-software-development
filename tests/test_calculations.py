from geo_calculator.calculations import find_average
from geo_calculator.calculations import (
    gardners_equation,
    inverse_gardners_equation,
)
import pytest


def test_find_average() -> None:
    numbers = [2, 4, 6, 8]
    result = find_average(numbers)
    assert result == 5


def test_gardners_equation() -> None:
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)

    
def test_inverse_gardners_equation() -> None:
    density = 2.0730949  # g/cm3
    expected_velocity = 2000  # m/s

    assert inverse_gardners_equation(density) == pytest.approx(
        expected_velocity
    )

    assert inverse_gardners_equation(
        gardners_equation(expected_velocity)
    ) == pytest.approx(expected_velocity)

    assert gardners_equation(
        inverse_gardners_equation(density)
    ) == pytest.approx(density)


def test_gardners_equation_negative_velocity() -> None:
    velocity = -1000

    with pytest.raises(ValueError):
        gardners_equation(velocity)


def test_inverse_gardners_equation_negative_density() -> None:
    density = -1000

    with pytest.raises(ValueError):
        inverse_gardners_equation(density)
