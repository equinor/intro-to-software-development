def find_average(numbers: list) -> float:
    return sum(numbers)/len(numbers)

def gardners_equation(velocity: float) -> float:
    return 0.31*(velocity**0.25)