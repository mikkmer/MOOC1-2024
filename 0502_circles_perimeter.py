"""Circle's perimeter."""
import math


def calculate_perimeter_of_a_circle(radius: int) -> float:
    """Return the perimeter of a circle."""
    # Your code goes here
    circle_perimeter = round(math.pi * 2 * radius, 2)
    return circle_perimeter