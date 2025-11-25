def factorial(n):
    """Compute n! for non-negative integer n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
