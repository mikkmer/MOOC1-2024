"""Capitalize and replace letters in string."""


def modify_string(phrase: str) -> str:
    """
    Return a modified version of the string with certain letters capitalized and replaced.

    First letter of the string must be capitalized.
    All occurrences of the letters: a,e,i,o,u must be capitalized.
    """
    # Write your code here
    modified_string = []

    letters = "aeiou"
    for char in phrase:
        if char.lower() in letters:
            modified_string.append(char.upper())
        else:
            modified_string.append(char)
    
    if not modified_string:
        return ""
    result = "".join(modified_string)
    return result[0].upper() + result[1:]

print(modify_string(""))