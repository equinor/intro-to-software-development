# Implement Gardner's equation

## Gardner's equation

Now that we have our package structure, a working ci workflow and decent tooling in place, we are ready to add some features to our package.

We will be implementing a formula called Gardner's equation.

"This equation is very popular in petroleum exploration because it can provide information about the lithology from interval velocities obtained from seismic data." - https://en.wikipedia.org/wiki/Gardner%27s_relation

- Start with adding this test to `test_calculations.py`:

```python
def test_gardners_equation() -> None:
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)
```

- Remember to import the function and `pytest` at the top of the test file:
  `from geo_calculator.calculations import gardners_equation` and `import pytest`.

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
  - `git switch main` and `git rebase origin/main`
  - `git switch -c implement-gardners-equation`
  - `git add -p`
  - `git commit -m "Add gardners equation"`
- Note: It is good to keep the tests and the implementation in the same commit. Ideally, every commit should be able to stand on its own, i.e. the tests should pass in each commit.

## Add docstrings to function implementation

- "A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition." - [PEP257](https://peps.python.org/pep-0257/)
- There are different styles for Python docstrings. The following examples use [Google Style Docstrings](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods), but there are also NumPy Style and Sphinx Style.

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

- One of the requirements we may have to the function is that it should handle all kinds of input (through the argument). In this case, for example, it does not make sense to return any value if the velocity is negative, as this would have led to negative density. We may figure it is better to throw a `ValueError` in this case.
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

## Bonus: test many values at once with `parametrize`

Instead of writing one test per input, `pytest` lets you run the same test body over many
inputs with `@pytest.mark.parametrize`. This is a clean way to cover several cases:

```python
import pytest

from geo_calculator.calculations import gardners_equation


@pytest.mark.parametrize(
    "velocity, expected_density",
    [
        (2000, 2.0730949),
        (3000, 2.2942567),
        (4000, 2.4653393),
    ],
)
def test_gardners_equation_multiple_values(
    velocity: float, expected_density: float
) -> None:
    assert gardners_equation(velocity) == pytest.approx(expected_density)
```

- Run `pytest -v` and notice that each parameter set shows up as its own test.

## Bonus: edge case at zero velocity

- We already reject negative velocities. What should happen at exactly `velocity = 0`?
  Decide on the desired behaviour, add a test that documents it, and make it pass:

```python
def test_gardners_equation_zero_velocity() -> None:
    assert gardners_equation(0) == pytest.approx(0)
```

## Bonus: vectorize with NumPy

`numpy` is already a dependency of the package, but we have not used it yet. In real
geoscience work you rarely have a single velocity — you have a whole seismic trace. NumPy
lets the same equation operate on a whole array at once, which is both shorter to write
and much faster than a Python loop. This is a small taste of the Data Science part of the
course (Day 3).

- Add a test that passes an array of velocities and expects an array of densities:

```python
import numpy as np


def test_gardners_equation_array_input() -> None:
    velocities = np.array([2000, 3000, 4000])
    expected = np.array([2.0730949, 2.2942567, 2.4653393])

    result = gardners_equation(velocities)

    np.testing.assert_allclose(result, expected, rtol=1e-6)
```

- If you implemented `gardners_equation` with `**` and basic arithmetic, it may already work
  on arrays thanks to NumPy broadcasting. If you used input validation like `if velocity < 0`,
  you will need to adapt it to work element-wise (hint: `np.any(velocity < 0)`).
