from hw2_debugging import mergeSort

def test_sort_empty():
    assert mergeSort([]) == []

def test_sort_single_element():
    assert mergeSort([1]) == [1]

def test_sort_multiple_elements():
    assert mergeSort([4, 2, 7, 1, 9]) == [1, 2, 4, 7, 9]

def test_sort_duplicates():
    assert mergeSort([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]

def test_sort_reverse_order():
    assert mergeSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
