#!/usr/bin/python3
"""
Module to calculate the minimum operations to achieve n characters using
only "Copy All" and "Paste" operations.
"""


def processFactors(num):
    """Calculate the factors that help reduce the number to 1."""
    factor_count = 1
    factor_list = []
    current_val = num

    while current_val > 1:
        factor_count += 1
        if current_val % factor_count == 0:
            while current_val % factor_count == 0:
                current_val /= factor_count
                factor_list.append(factor_count)
    return factor_list


def minOperations(n):
    """
    Calculate the minimum number of operations required to reach n characters.
    """
    if n < 2:
        return 0

    steps = processFactors(n)
    return sum(steps)
