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
    if (velocity < 0):
        raise ValueError()
    return 0.31*(velocity**0.25)

def inverse_gardners_equation(density: float) -> float:
    """Calculates the inverse of the Gardner's equation
    Args:
        density: A float in g/cm3
    """
    if (density < 0):
        raise ValueError()
    return (density/0.31)**4