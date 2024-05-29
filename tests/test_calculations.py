from geo_calculator.calculations import find_average, numpy_find_average


def test_find_average():
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_average(numbers) == 3.5


def test_numpy_find_average():
    numbers = [1, 2, 3, 4, 5, 6]
    assert numpy_find_average(numbers) == 3.5
