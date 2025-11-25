def average(nums):
    """Return arithmetic mean of a list of numbers."""
    total = 0.0
    for x in nums:
        total += x
    return total / len(nums)
