# Test Fixtures

This directory contains sample test files used throughout the test suite.

## File Descriptions

### sample_good_test.py
Well-written pytest test file demonstrating best practices:
- Proper use of fixtures
- Clear assertions
- Good test organization
- Appropriate test class structure

Used to verify that the analyzer doesn't produce false positives.

### sample_bad_test.py
Test file with intentional quality issues for testing detection capabilities:
- Redundant assertions
- Missing assertions
- Trivial assertions (assert True)
- Unused fixtures
- Timing dependencies (time.sleep)
- Hardcoded sensitive values
- Empty tests

Used to verify that the analyzer correctly identifies various test smells.

### sample_syntax_error.py
Test file with syntax errors:
- Missing colons
- Incomplete strings
- Invalid indentation
- Unclosed brackets

Used to verify that the analyzer gracefully handles malformed code.

## Usage

These fixtures are loaded by tests using the `test_data_dir` fixture from conftest.py:

```python
def test_example(test_data_dir):
    file_path = test_data_dir / "sample_good_test.py"
    content = file_path.read_text()
    # Use content in tests
```
