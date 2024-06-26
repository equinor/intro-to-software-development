def find_average(nums: list[int]) -> float:
    return sum(nums) / len(nums)

def gardners_equation(velocity: int, alpha: float = 0.31, beta: float = 0.25) -> float:
    """Calculates the seismic P-wave velocity to the bulk density of the lithology in which the wave travels.
    Args:
        velocity: A number
    Returns:
        The bulk density
    """
    density = alpha * velocity ** beta
    return density