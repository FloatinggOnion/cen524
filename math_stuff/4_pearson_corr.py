# Algorithm for calculating the Pearson correlation coefficient
# between two lists of numbers.

# 1. Read the two lists of numbers, x and y.
# 2. Check if the lengths of the two lists are equal.
# 3. Calculate the means of x and y.
# 4. Calculate the covariance of x and y.
# 5. Calculate the standard deviations of x and y.
# 6. Calculate the Pearson correlation coefficient using the formula:
#    r = covariance(x, y) / (std_dev(x) * std_dev(y))
# 7. Return the Pearson correlation coefficient.
# 8. If the lengths of the two lists are not equal, return None.
# 9. If the lists are empty, return None.
# 10. If the lists contain non-numeric values, return None.