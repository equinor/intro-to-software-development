from typing import Sequence

def find_average(numbers: Sequence[int]) -> float:
    tot = 0
    for num in numbers:
        tot += num

    return tot/len(numbers)

def gardners_equation(velocity: float) -> float:
    rho = 0.23*velocity**(0.25)
    return rho