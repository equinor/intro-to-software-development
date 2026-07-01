from geo_calculator.calculations import find_average 
def test_length_of_string() -> None:
    test_string = "python"  # Arrange: set up the inputs
    length = len(test_string)  # Act: run the thing under test
    assert length == 6  # Assert: check the result


def test_find_average_given_list_of_numbers() -> None:
    list = [1, 2, 3]
    sum = 0
    for x in list:
        sum+=x
    res = sum/len(list)
    assert res == find_average(list)