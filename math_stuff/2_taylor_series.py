import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

# taylor series
def taylor_series(x, n):
    sum = 0
    for i in range(n):
        sum += (x**i) / factorial(i)
    return sum


# array of input terms and a is a real number
terms = [0, 1, 2, 3, 4]
a = 1.0

print("Taylor series expansion of e^x at x = 1.0")
for i in range(len(terms)):
    print("Term", terms[i], ":", taylor_series(a, terms[i]))