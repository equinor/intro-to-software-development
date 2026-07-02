
from geo_calculator.calculations import find_avrage

def test_find_average_given_list_of_number():
    list_of_num = [1, 2, 3, 4]
    sum=0
    for i in list_of_num:
        sum += i
    length = len(list_of_num)
    avrage = sum/length
    assert avrage == find_avrage(list_of_num)



def test_length_of_string() -> None:
    test_string = "python"  # Arrange: set up the inputs
    length = len(test_string)  # Act: run the thing under test
    assert length == 6  # Assert: check the result