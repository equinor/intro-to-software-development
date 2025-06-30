from geo_calculator.calculations import find_average


def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6

def test_find_average() -> None:
    testcase = [1,8,5,2]
    assert find_average(testcase) == 4
