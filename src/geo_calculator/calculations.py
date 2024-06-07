# Perform some calculations on the dataset
from typing import Iterable


def find_average(numbers: Iterable[float]) -> float:
    return sum(numbers) / len(numbers)


# Insert typical non-linear domain calculations
def gardners_equation(velocity: float, alpha=310.0, beta=0.25) -> float:
    """gardners equation

    https://en.wikipedia.org/wiki/Gardner%27s_relation

    TODO: Include doctest
    """

    if velocity < 0:
        raise ValueError(f"Velocity can not be negative, got {velocity}")

    density = alpha * velocity**beta
    return


# Make the inverse garners equation (compute velocity from density)
def inverse_gardners_equation(density: float):
    pass


# Shear velocity, Vs to density; if time
# https://en.wikipedia.org/wiki/Shear_modulus
