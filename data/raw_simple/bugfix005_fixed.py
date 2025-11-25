def max_in_list(values):
    """Return the maximum element in a non-empty list."""
    if not values:
        raise ValueError("list must not be empty")
    current_max = values[0]
    for v in values[1:]:
        if v > current_max:
            current_max = v
    return current_max
