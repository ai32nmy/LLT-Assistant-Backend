def safe_get(lst, index, default=None):
    """Return lst[index] if in range, otherwise default."""
    # Support Python's negative indices semantics
    if -len(lst) <= index < len(lst):
        return lst[index]
    return default
