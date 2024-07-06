#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generates the Pascal's triangle up to the n-th row.

    Args:
        n (int): The number of rows to generate in the Pascal's triangle.

    Returns:
        list: A list containing the rows of the Pascal's triangle.
    """
    if n <= 0:
        return[]
    Triangle = [[1]]
    for i in range(1, n):
        row = next_row(Triangle[-1])
        Triangle.append(row)
    return Triangle


def next_row(current_row):
    """
    Generates the next row of the Pascal's triangle from the current row.

    Args:
        current_row (list): The current row of the Pascal's triangle.

    Returns:
        list: The next row of the Pascal's triangle.
    """
    new_row = [1]
    for i in range(len(current_row) - 1):
        new_row.append(current_row[i] + current_row[i+1])
    new_row.append(1)
    return new_row
