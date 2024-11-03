"""Hola string."""


def hola_string(count: int) -> str:
    """
    Make hola string.

    print(hola_string(3)) => "holaholahola"
    print(hola_string(0)) => ""

    :param count: number of times to repeat
    :return: The string "hola" repeated `count` times.
    """
    # Write your code here needs to use while loop
    temp = ""
    while count > 0:
        temp += "hola"
        count -= 1
    return temp
