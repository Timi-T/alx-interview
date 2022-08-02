#!/usr/bin/python3
"""
Rotate a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """Function to rotate a 2d matrix in place"""

    n = len(matrix)
    for i in range(n):
        j = 0
        while j + i < n:
            temp = matrix[i][j + i]
            matrix[i][j + i] = matrix[j + i][i]
            matrix[j + i][i] = temp
            j += 1

    for i in range(n):
        a = 0
        b = n - 1
        while a < b:
            temp = matrix[i][a]
            matrix[i][a] = matrix[i][b]
            matrix[i][b] = temp
            a += 1
            b -= 1
