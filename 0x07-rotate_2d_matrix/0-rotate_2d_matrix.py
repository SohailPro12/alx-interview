#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_rows(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i].reverse()


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    transpose(matrix)
    reverse_rows(matrix)
