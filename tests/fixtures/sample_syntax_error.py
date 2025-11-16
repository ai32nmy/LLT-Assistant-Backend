"""
Sample pytest test file with syntax errors.

This file is intentionally malformed to test error handling.
"""

def test_missing_colon(
    # Missing colon in function definition
    assert True


def test_incomplete_string():
    value = "incomplete string
    assert value is not None


def test_invalid_indentation():
    result = 1 + 1
  assert result == 2  # Incorrect indentation


def test_unclosed_bracket():
    data = [1, 2, 3
    assert len(data) == 3
