def normalize_list(values):
    """Scale values so that the maximum absolute value becomes 1."""
    if not values:
        raise ValueError("values must not be empty")
    max_abs = 0.0
    for v in values:
        if abs(v) > max_abs:
            max_abs = abs(v)
    return [v / max_abs for v in values]
