from geo_calculator.calculations import find_average

def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6

def test_find_average_of_list() -> None:
    liste = [1,2,3]
    assert find_average(liste) == 2