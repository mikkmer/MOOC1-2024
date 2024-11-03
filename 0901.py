"""Contains digit."""


def contains_digit(some_string: str) -> bool:
    """
    Check if a given string contains at least one digit.

    :parm some_string: given string
    :return: Return True if the input string contains a digit, False otherwise.
    """
    # Write your code here
    for i in some_string:
        if i.isdigit():
            return True
    return False
