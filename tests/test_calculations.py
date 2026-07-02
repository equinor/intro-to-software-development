import pytest

from geo_calculator.calculations import find_average, gardners_equation


def test_length_of_string() -> None:
    test_string = "python"  # Arrange: set up the inputs
    length = len(test_string)  # Act: run the thing under test
    assert length == 6  # Assert: check the result


def test_find_average_given_list_of_numbers() -> None:
    test_list = [1, 2, 3, 4, 5]
    results = find_average(test_list)
    assert results == 3


def test_gardners_equation() -> None:
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)
