def find_average(data_list: list) -> float:
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """

    sum = 0
    for i in data_list:
        sum += i
    return sum/len(data_list)

def gardners_equation(velocity) -> float:
    """Calculate the seismic p-wave velocity from the bulk density of the lithology in which the wave travels.
    Args:
        Velocity
    Returns:
        Seismic p-wave velocity
    """

    return 0.31*(velocity**0.25)