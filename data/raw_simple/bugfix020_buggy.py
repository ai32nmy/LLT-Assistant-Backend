def median_of_three(a, b, c):
    """Return the median (middle) value among a, b, and c."""
    # BUG: logic incorrectly swaps for some orderings
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    return c
