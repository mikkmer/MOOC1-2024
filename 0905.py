"""Sum of even numbers in the range."""


def sum_of_even_numbers_in_range(n: int) -> int:
    """
    Return sum of even numbers from 0 up to n (included).

    print(sum_of_even_numbers_in_range(5)) => 0 + 2 + 4 = 6
    print(sum_of_even_numbers_in_range(0)) => 0

    :param n: inclusive upper limit of range
    :return: Sum of even numbers from 0 to n.
    """
    # Write your code here
    sum = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            sum += i
    return sum
