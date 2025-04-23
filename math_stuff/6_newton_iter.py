def newton_reciprocal(N, x0, iterations):
    """
    Newton's Iterative Formula to find the reciprocal of a number N.
    Formula: x_(i+1) = x_i * (2 - x_i * N)
    
    Args:
        N (float): The number whose reciprocal is to be found.
        x0 (float): Initial guess for the reciprocal.
        iterations (int): Number of iterations to perform.
    
    Returns:
        None: Prints the value of x at each iteration.
    """
    xi = x0
    print(f"Initial guess x0: {xi}")
    for i in range(iterations):
        xi = xi * (2 - xi * N)
        print(f"Iteration {i + 1}: x = {xi}")
    print(f"Approximate reciprocal of {N} after {iterations} iterations: {xi}")

# Parameters
N = 5  # The number whose reciprocal is to be found
x0 = 0.1  # Initial guess
iterations = 10  # Number of iterations

# Run the algorithm
newton_reciprocal(N, x0, iterations)