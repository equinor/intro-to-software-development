from typing import Sequence

def find_average(numbers: Sequence[int]) -> float:
    return sum(numbers) / len(numbers)

def use() -> None:
    my_average: float = find_average([1,2,3])
    print(my_average)

if __name__ == "__main__":
    use()