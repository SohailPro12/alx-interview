#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return
    Triangle = [[1]]
    for i in range(1, n):
        row = next_row(Triangle[-1])
        Triangle.append(row)
    return Triangle


def next_row(current_row):
    new_row = [1]
    for i in range(len(current_row) - 1):
        new_row.append(current_row[i] + current_row[i+1])
    new_row.append(1)
    return new_row
