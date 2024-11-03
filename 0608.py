"""Ask name and greet."""
# https://stackoverflow.com/questions/50192965/how-to-make-user-input-not-case-sensitive


def ask_name_and_greet():
    """
    Ask for the user's name and greet them.

    The user has to enter his/her name. The function prints the greeting.

    Regular greeting: Hi, [name]. Would you like to have a Hamburger?
    [name] is capitalized, meaning first letter is capital, the rest is lower.

    If the name is Thanos (case-insensitive, so thanos and THANOS also count):
    Get out of here, Thanos! Nobody wants to play with you!
    """
    # Your code goes here
    name = input().lower()
    if name == "thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {name.capitalize()}. Would you like to have a Hamburger?")

ask_name_and_greet()