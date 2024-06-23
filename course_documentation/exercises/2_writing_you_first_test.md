# Writing your first test

## Add test

- Create /tests/test_calculations.py

```python
from geo_calculator.calculations import find_average

def test_find_average_given_a_list_of_ints():
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_average(numbers) == 3.5
```

## Install and run tests

- pip install pytest
- pytest
- See that the test fails

## Make test pass

- Up to you now...
