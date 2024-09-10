from binary_search import binary_search
import pytest

# Passing test case


def test_binary_search_pass():
    arr = [1, 2, 3, 4, 5]
    search_value = 3
    expected_result = 2
    assert binary_search(
        arr, search_value) == expected_result, "Test case passed"

# Failing test case


def test_binary_search_fail():
    arr = [1, 2, 3, 4, 5]
    search_value = 6
    expected_result = 4  # Wrong index to fail the test case.
    assert binary_search(
        arr, search_value) == expected_result, "Test case failed"
