import pytest
from geo_calculator.calculations import find_average, gardners_equation


def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6

def test_find_average() -> None:
    testcase = [1,8,5,2]
    assert find_average(testcase) == 4

def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)