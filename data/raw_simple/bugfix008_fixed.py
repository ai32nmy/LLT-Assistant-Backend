def remove_duplicates(items):
    """Return a new list with duplicates removed, keeping first occurrence."""
    seen = []
    result = []
    for x in items:
        if x not in seen:
            seen.append(x)
            result.append(x)
    return result
