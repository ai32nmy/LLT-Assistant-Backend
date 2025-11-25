def average(nums):
    """Return arithmetic mean of a list of numbers."""
    if not nums:
        raise ValueError("cannot compute average of empty list")
    total = 0.0
    for x in nums:
        total += x
    return total / len(nums)
