# Perform some calculations for use on lithology datasets


from typing import Sequence


def find_average(numbers: Sequence[int]) -> float:
    """Calculate the average of some numbers
    Args:
        numbers (Sequence[int]): A sequence of numbers
    Returns:
        (float): The average value of the numbers
    """
    return sum(numbers) / len(numbers)


def gardners_equation(
    velocity: float, alpha: float = 0.31, beta: float = 0.25
) -> float:
    """Calculate bulk density of lithology based on seismic P-wave velocity

    Args:
        velocity (float): Seismic P-wave velocity in m/s.
        alpha (float): Empirically derived constant.
        beta (float): Empirically derived constant.
    Returns:
        density (float): Bulk density in g/cm3.
    Raises:
        ValueError: If the velocity is negative.

    Read more about gardners equation here:
    https://en.wikipedia.org/wiki/Gardner%27s_relation
    """

    if velocity < 0:
        raise ValueError(f"Velocity can not be negative, got {velocity}")

    density: float = alpha * velocity**beta
    return density


def inverse_gardners_equation(
    density: float, alpha: float = 0.31, beta: float = 0.25
) -> float:
    """Calculate seismic P-wave velocity based on bulk density of lithology

    Args:
        density (float): Bulk density in g/cm3.
        alpha (float): Empirically derived constant.
        beta (float): Empirically derived constant.
    Returns:
        velocity (float): Seismic P-wave velocity in m/s.
    Raises:
        ValueError: If the density is negative.

    """

    if density < 0:
        raise ValueError(f"Density can not be negative, got {density}")

    velocity: float = (density / alpha) ** (1 / beta)
    return velocity
