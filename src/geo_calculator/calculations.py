from typing import List

def find_average(numbers: List[int | float]) -> float:
    return sum(numbers) / len(numbers)

def gardners_equation(velocity: float) -> float:
    return 0.31 * velocity^0.25