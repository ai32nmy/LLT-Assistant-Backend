def count_occurrences(values, target):
    """Return how many times target appears in values."""
    count = 0
    for v in values:
        if v == target:
            count += 1
    return count
