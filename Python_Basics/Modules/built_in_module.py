# In Python, code is often organized into files and folders so it can be reused easily.
# That’s where modules and packages come in.

# A module is simply a Python file (.py) that contains functions, classes, or variables.
# We use import to bring the module into our program.

import math

print(math.sqrt(25))   # Square root
print(math.pi)         # Value of π
print(math.factorial(5))  # Factorial of 5


# Import entire module
import math
print(math.sqrt(16))

# Import specific function
from math import sqrt
print(sqrt(16))

# Import with alias
import math as m
print(m.sqrt(16))

# Import everything (not recommended)
from math import *
print(sqrt(16))
