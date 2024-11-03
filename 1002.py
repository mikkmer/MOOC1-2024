"""Create new list with added number."""


def create_new_list_with_added_number(numbers: list, number: int) -> list:
    """
    Return a new list with the number added to it.

    Do not modify the existing list.
    add_element_into_list([1, 2, 3], 4) => [1, 2, 3, 4]
    """
    # Write your code here
    new_list = numbers.copy()
    new_list.append(number)
    return new_list
