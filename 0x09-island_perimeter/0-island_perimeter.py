#!/usr/bin/python3
"""
Island perimeter module
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    rows = len(grid)
    cols = len(grid[0])
    permiter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i > 0 and grid[i-1][j] == 0:
                    permiter += 1
                if j > 0 and grid[i][j-1] == 0:
                    permiter += 1
                if i < rows - 1 and grid[i+1][j] == 0:
                    permiter += 1
                if j < cols - 1 and grid[i][j+1] == 0:
                    permiter += 1
    return permiter
