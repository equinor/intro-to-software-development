# Implement Gardner's equation

## Gardner's equation

Now that we have our package structure, a working ci workflow and decent tooling in place, we are ready to add some features to our package.

We will be implementing a formula called Gardner's equation.

"This equation is very popular in petroleum exploration because it can provide information about the lithology from interval velocities obtained from seismic data." - https://en.wikipedia.org/wiki/Gardner%27s_relation

- Start with adding this test to `test_calculations.py`:

```python
def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)

```

- Run the tests with `pytest` and verify that they fail.

## Make the test pass

- Up to you now...
- Implement the equation from the wikipedia article and make the test pass.
- Experiment with different relative and absolute tolerances in the approximation

<!-- ```python
    # These fail
    assert gardners_equation(velocity) == pytest.approx(expected_density, rel=1e-8)
    assert gardners_equation(velocity) == pytest.approx(expected_density, abs=1e-8)
    # These pass
    assert gardners_equation(velocity) == pytest.approx(expected_density, rel=1e-7)
    assert gardners_equation(velocity) == pytest.approx(expected_density, abs=1e-7)
``` -->

- Commit your work. Since this is a new feature, it may make sense with a new branch.
  - `git fetch origin`
  - `git checkout origin/main` or (`git checkout main` and `git rebase origin/main`)
  - `git checkout -b implement-gardners-equation`
  - `git add -p`
  - `git commit -m "Add gardners equation"`
- Note: It is good to keep the tests and the implementation in the same commit. Ideally, every commit should be able to stand on its own, i.e. the tests should pass in each commit.

## Add docstrings to function implementation

- "A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition." - [PEP257](https://peps.python.org/pep-0257/)
- There are different styles for Python docstrings. The following examples uses [Google Style Docstrings](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods), but there are also NumPy Style and Spinx Style.

- For the `find_average` function the docstring may look something like this:

```python
def find_average(numbers: Sequence[int]) -> float:
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    return sum(numbers) / len(numbers)
```

- Ex: Write a good description, including arguments and return value, and write it in the docstring for the `gardners_equation` function:

```python
def gardners_equation(...):
    """Calculate <fill inn here>"""
```

- Commit your work
  - `git add -p`
  - `git commit -m "Add docstrings"`

## Implement inverse gardners equation

- This can sometimes be what you need. In addition, it makes it possible to write an inverse test, testing both implementations at once.
- Start with adding a test for this:

```python
def test_inverse_gardners_equation() -> None:
    density = 2.0730949  # g/cm3
    expected_velocity = 2000  # m/s

    assert inverse_gardners_equation(density) == pytest.approx(expected_velocity)

    assert inverse_gardners_equation(
        gardners_equation(expected_velocity)
    ) == pytest.approx(expected_velocity)

    assert gardners_equation(inverse_gardners_equation(density)) == pytest.approx(
        density
    )
```

## Sanitize input for negative values

- One of the requirements we may have to the function is that it should handle all kinds of input (through the argument). In this case, for example, it does not make sense to return any value if the velocity is negative, as this would have led to negative density. We may figure it is better to through a `ValueError` in this case.
- First, add the following tests to `test_calculations.py`

```python
def test_gardners_equation_negative_velocity() -> None:
    velocity = -1000  # m/s
    with pytest.raises(ValueError) as e:
        gardners_equation(velocity)


def test_inverse_gardners_equation_negative_density() -> None:
    density = -1000  # g/cm3
    with pytest.raises(ValueError) as e:
        inverse_gardners_equation(density)
```

- Exercise: Add implementation to make the tests pass
- Commit your work and make PR
  - `git add -p`
  - `git commit -m "Implement inverse gardner's equation"`
  - `git push origin implement-gardners-equation`
