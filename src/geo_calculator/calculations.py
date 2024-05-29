# Perform some calculations on the dataset
import numpy as np


def find_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def numpy_find_average(numbers: list[float]) -> float:
    return np.average(numbers)
