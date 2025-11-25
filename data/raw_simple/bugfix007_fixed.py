def is_palindrome(s):
    """Return True if s is a palindrome (exact match, case-sensitive)."""
    return s == s[::-1]
