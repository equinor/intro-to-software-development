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
    return 0.31 * velocity ** (1 / 4)
