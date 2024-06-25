from geo_calculator.calculations import find_average
from geo_calculator.calculations import gardners_equation
import pytest


def test_find_average_given_a_list_of_ints() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_average(numbers) == 3.5

def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)
