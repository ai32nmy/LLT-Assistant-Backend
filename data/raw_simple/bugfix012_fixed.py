def index_of_min(values):
    """Return the index of the minimum element in a non-empty list."""
    if not values:
        raise ValueError("list must not be empty")
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index
