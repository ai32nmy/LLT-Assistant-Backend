def average_even_numbers(values):
    """Return the average of even numbers in the list."""
    if not values:
        raise ValueError("list must not be empty")
    total = 0
    count = 0
    for v in values:
        if v % 2 == 1:
            total += v
            count += 1
    if count == 0:
        raise ValueError("no even numbers in list")
    return total / count
