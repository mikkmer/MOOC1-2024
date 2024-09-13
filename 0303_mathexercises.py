"""Math exercises."""
import math

# Your code goes here

# Time converter
seconds = 37810
hours = seconds // 3600
minutes = (seconds % 3600) // 60

# Trigonometry calculator
angle = 339
sine = round(math.sin(math.radians(angle)), 1)
cosine = round(math.cos(math.radians(angle)), 1)

# Greetings
lots_of_heys = "Hey" * 87

# Adding numbers
string_numbers = "81" + "69"

# print all
print(hours, minutes, sine, cosine, lots_of_heys, string_numbers)
