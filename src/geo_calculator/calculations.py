def find_average(list: list) -> float:
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    return sum(list) / len(list)


def gardners_equation(velocity: float) -> float:
    """Calculate the density
    Args:
        velocity: A float in m/s
    Returns:
        The density
    """
    if velocity < 0:
        raise ValueError
    return 0.31 * velocity ** (1 / 4)


def inverse_gardners_equation(density: float) -> float:
    """Calculate the velocity
    Args:
        density: A density in g/cm3
    Returns:
        The Velocity
    """
    if density < 0:
        raise ValueError
    return (density / 0.31) ** 4
