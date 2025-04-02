import math
# factorial

# Algorithm:
# 1. Read n
# 2. Compute factorial = 1
# 3. For i from 1 to n:
#    a. factorial = factorial * i
# 4. Print factorial

# Implementation
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Test the function
print(factorial(5) == math.factorial(5))