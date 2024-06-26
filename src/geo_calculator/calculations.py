from typing import Sequence


def find_average(numbers: Sequence[int]) -> float:
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    return sum(numbers) / len(numbers)


def gardners_equation(velocity: float) -> float:
    """Calculate bulk densisty of the lithology
    Args:
        Velocity: a float 
    Returns: 
        The density
    """
    alfa: float = 0.31
    beta: float  = 0.25
    return alfa * velocity**beta
