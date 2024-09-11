# sorting an empty array, a single element array, multiple elements, duplicates, and a reverse-ordered array.
from hw2_debugging import merge_sort


def test_sort_empty():
    assert merge_sort([]) == []


def test_sort_single_element():
    assert merge_sort([1]) == [1]


def test_sort_multiple_elements():
    assert merge_sort([4, 2, 7, 1, 9]) == [1, 2, 4, 7, 9]


def test_sort_duplicates():
    assert merge_sort([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]


def test_sort_reverse_order():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
