def safe_get(lst, index, default=None):
    """Return lst[index] if in range, otherwise default."""
    if index < 0 or index >= len(lst):
        return default
    return lst[index]
