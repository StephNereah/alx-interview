#!/usr/bin/python3
"""
0-pascal_triangle module
Defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal Triangle of n.
    
    Args:
        n (int): The number of rows in the Pascal's triangle.
    
    Returns:
        list: A list of lists where each list represents a row of Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            temp.append(k[i - 1][j] + k[i - 1][j + 1])
        temp.append(1)
        k.append(temp)
    return k