def find_average(numbers: list) -> float:
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    return sum(numbers) / len(numbers)

def gardners_equation(velocity: float) -> float:
    """Calculates Gardner's equation
    Args:
        velocity: A float in m/s
    """
    return 0.31*(velocity**0.25)