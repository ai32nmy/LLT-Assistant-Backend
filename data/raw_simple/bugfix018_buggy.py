def is_anagram(a, b):
    """Return True if a and b are anagrams (case-sensitive)."""
    counts = {}
    for ch in a:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in b:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    return True
