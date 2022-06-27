#!/usr/bin/python3
"""
This module handles minimum operations for a task
"""

import math


def minOperations(n):
    """
    Function to find minimum operations for a copy and paste operation
    given a maximum of 2 operations;
    1. Copyall
    2. Paste
    """

    if n <= 1:
        return 0
    if n == 2 or n == 3:
        return n
    for i in range(2, n + 1):
        if n % i == 0:
            lcm = i
            break
    if lcm == n:
        return n
    return minOperations(int(n / lcm)) + lcm
