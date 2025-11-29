# A package is a collection of modules stored in a folder.
# It must contain a special file called __init__.py (can be empty).
# Helps in organizing larger projects.

from math_operations import addition, subtraction

print(addition.add(10, 5))
print(subtraction.subtract(10, 5))
