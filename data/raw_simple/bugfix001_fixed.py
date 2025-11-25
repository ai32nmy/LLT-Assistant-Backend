def sum_first_n(nums, n):
    """Return sum of the first n elements of nums."""
    if n < 0:
        raise ValueError("n must be non-negative")
    total = 0
    for i in range(n):
        if i >= len(nums):
            break
        total += nums[i]
    return total
