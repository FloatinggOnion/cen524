# Code for sum of a geometric progression/series
import math

# Algorithm
# 1. Read a, r, n
# 2. Compute sum = a * (1 - r**n) / (1 - r) if r < 1
# 3. Compute sum = a * (r**n - 1) / (r - 1) if r > 1
# 4. Compute a / (1 - r) if n = infinity and r < 1
# 5. Print sum

# Implementation
a = float(input("Enter first term: "))
r = float(input("Enter common ratio: "))
n = int(input("Enter number of terms: "))

def gp_sum(a, r, n):
    if r == 1:
        return a * n
    elif r < 1:
        return a * (1 - r**n) / (1 - r)
    elif n == math.inf and r < 1:
        return a / (1 - r)
    else:
        return a * (r**n - 1) / (r - 1)
    

print("Sum of the geometric progression is", gp_sum(a, r, n))