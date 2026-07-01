from geo_calculator.calculation import find_average


def test_find_average_returns_expected_value() -> None:
	numbers = [1, 2, 3, 4, 5, 6, 7]
	average = find_average(numbers)
	assert average == 4.0