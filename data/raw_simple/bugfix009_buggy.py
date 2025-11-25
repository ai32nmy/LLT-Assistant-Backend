def fib(n):
    """Return the n-th Fibonacci number (0-based)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
