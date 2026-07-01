from geo_calculator.calculations import find_average


def test_find_average() -> None:
    numbers = [2, 4, 6, 8]
    result = find_average(numbers)
    assert result == 5
