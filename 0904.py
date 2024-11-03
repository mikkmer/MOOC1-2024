"""Sum of range."""


def sum_of_numbers_in_range(start: int, end: int) -> int:
    """
    Return the sum of integers between start and end (both included).

    print(sum_of_numbers_in_range(3, 5)) => 3 + 4 + 5 = 12
    print(sum_of_numbers_in_range(5, 5)) => 5

    :param start: start of inclusive range
    :param end: end of inclusive range
    :return: Sum of integers between start and end.
    """
    # Write your code here
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum
