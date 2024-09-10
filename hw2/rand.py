"""
rand.py

This module contains random_array function, which generates random numbers from 1 to 20.
Date: 2024-09-10
"""
import subprocess


def random_array(arr):
    """
    Generates a random integer between 1 and 20.

    Returns:
        arr: list of random integers.
    """
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
