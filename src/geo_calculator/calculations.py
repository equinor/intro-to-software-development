from typing import Sequence


def find_average(numbers: Sequence[int]) -> float:
    """
    Finds the average number out of a sequence of numbers.
    """
    return sum(numbers) / len(numbers)


def use() -> None:
    my_average: float = find_average([1, 2, 3])
    print(my_average)

def gardners_equation(vel) -> float:
    """
    Takes in the P-wave velocity in m/s, and returns the bulk density in g/cm^3
    Args:
        vel = the P-wave velocity in m/s
    Returns:
        The bulk density in g/cm^3
    """
    if vel<0:
        raise ValueError(f"Negative velocity value is not physical/possible. Got {vel}.")
    return 0.31*vel**(0.25)

def inverse_gardners_equation(dense) -> float:
    """
    Inverse gardners equation, finds velocity with density input
    """
    if dense<0:
        raise ValueError(f"Negative density is not physical, and the input was {dense}")
    return (dense/0.31)**4

if __name__ == "__main__":
    use()
