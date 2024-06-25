from typing import Sequence

def find_average(num_list: Sequence[int]) -> float:
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    if len(num_list) == 0:
        return 0
    average = 0
    for i in num_list:
        average += i
    return average / len(num_list)

def gardners_equation(velocity: int) -> float:
    """ Calculate bulk density given in g/cm^3, based on a velocity
    Args:
        velocity: float of the velocity in m/s
    Returns:
        Bulk density in g/cm^3
    """
    return 0.31*(velocity**(0.25))
