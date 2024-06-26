from typing import Sequence


def find_average(numbers: Sequence[int]) -> float:
    """
    Finds the average number out of a sequence of numbers.
    """
    return sum(numbers) / len(numbers)


def use() -> None:
    my_average: float = find_average([1, 2, 3])
    print(my_average)

def gardners_equation(vel):
    """
    Takes in the P-wave velocity in m/s, and returns the bulk density in g/cm^3
    """
    return 0.31*vel**(0.25)

if __name__ == "__main__":
    use()
