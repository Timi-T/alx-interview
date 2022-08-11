#!/usr/bin/python3

"""Module to make change given coins and a target value"""


def makeChange(coins, total):
    """Function to calculate minimum change"""
    coins.sort(reverse=True)
    rem = total
    solution = 0
    i = 0
    change = 0
    if not total or total < 0:
        return 0
    while i < len(coins):
        j = i
        while j < len(coins):
            if coins[j] <= rem:
                change += int((str(rem / coins[j]).split('.'))[0])
                rem = rem % coins[j]
                if rem == 0:
                    if not solution:
                        solution = change
                    elif change < solution:
                        solution = change
                    break
                else:
                    j += 1
            else:
                j += 1
        i += 1
        rem = total
        change = 0
    if solution:
        return solution
    else:
        return -1
