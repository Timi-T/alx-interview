#!/usr/bin/python3

"""Module to calculate island perimeter"""


def island_perimeter(grid):
    """Function to calculate island perimeter"""

    perimeter = 0
    i = 0
    j = 0

    for i in range(len(grid)):
        sides = 0
        row = grid[i]
        for j in range(len(row)):
            if row[j]:
                if not j:
                    sides += 1
                if j == len(row) - 1:
                    sides += 1
                if not i:
                    sides += 1
                if i == len(grid) - 1:
                    sides += 1
                if j:
                    if not row[j - 1]:
                        sides += 1
                if i:
                    if not grid[i - 1][j]:
                        sides += 1
                if j != len(row):
                    if not row[j + 1]:
                        sides += 1
                if i != len(grid) - 1:
                    if not grid[i + 1][j]:
                        sides += 1
        perimeter += sides
    return perimeter
