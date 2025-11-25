def clamp(value, min_value, max_value):
    """Clamp value to the inclusive range [min_value, max_value]."""
    if value < min_value:
        return max_value
    if value > max_value:
        return min_value
    return value
