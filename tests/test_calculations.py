from geo_calculator.calculations import find_average

def test_find_average_given_list_of_numbers():
    numbers = [1,2,3,4,5,6]

    result = find_average(numbers)

    assert result == 3.5

