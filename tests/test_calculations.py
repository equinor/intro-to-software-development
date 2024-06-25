from geo_calculator.calculations import find_average

def test_find_average_given_a_list_of_ints() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_average(numbers) == 3.5


 