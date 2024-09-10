"""
hw2_debugging.py

This module contains code for sorting list, and uses rand.py to generate random numbers.
Date: 2024-09-10
"""
import rand

def merge_sort(arr):
    """
    Merge sort code
    Return:
        Sorted list
    """
    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Combine subproblems
    Return:
        Sorted list
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


random_arr = rand.random_array([None] * 20)
arr_out = merge_sort(random_arr)

print(arr_out)
