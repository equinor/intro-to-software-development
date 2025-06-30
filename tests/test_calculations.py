from geo_calculator.calculations import find_average

def test_lenght_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6

def test_find_avrage_of_list_of_numbers() -> None:
    test_list = [1,2,3,4,5,6]
    assert find_average(test_list) == 3.5
