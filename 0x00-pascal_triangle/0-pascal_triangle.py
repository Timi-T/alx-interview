#!/usr/bin/python3
"""
Implementation of pascal's triangle
"""


def pascal_triangle(n):
    """
    Function to return a list of lists representing each row of the triangle
    """
    if n <= 0:
        return []
    # Creating a list and including the first row as a list
    ret_list = [[1]]
    # Making an iteration for the number of rows for the triangle
    for i in range(n - 1):
        """
        Making a temporary array that adds a zero to the beginning
        and end of the last appended row
        """
        temp_arr = [0] + ret_list[-1] + [0]
        row = []
        # Iterating through the temporary array
        for j in range(len(temp_arr) - 1):
            row.append(temp_arr[j] + temp_arr[j + 1])
        # Append the new row to the list of lists
        ret_list.append(row)
    return ret_list
