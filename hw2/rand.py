"""
rand.py

This module contains random_array function, which generates random numbers from 1 to 20.
Date: 2024-09-10
"""
import secrets


def random_array(arr):
    """
    Generates a random integer between 1 and 20.

    Returns:
        arr: list of random integers.
    """
    for i in range(len(arr)):
        arr[i] = secrets.randbelow(20) + 1
    return arr
