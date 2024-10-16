#!/usr/bin/python3
"""Pascal Triangle Module."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.
    
    Args:
        n (int): The number of rows in Pascal's triangle.
    
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [0] * n

    for i in range(n):
        new_row = [0] * (i + 1)
        new_row[0] = 1
        new_row[-1] = 1

        for j in range(1, i):
            a = triangle[i - 1][j]
            b = triangle[i - 1][j - 1]
            new_row[j] = a + b

        triangle[i] = new_row

    return triangle