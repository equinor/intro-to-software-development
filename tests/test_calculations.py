from geo_calculator.calculations import find_average
def test_length_of_string() -> None:
    test_string = "python"

    length = len(test_string)

    assert length == 6


def test_find_average_given_list_of_numbers() -> None:
    input_numbers = [1,2,3,4,5,6]
    
    result = find_average(input_numbers)
    
    assert result == 3.5
