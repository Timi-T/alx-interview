#!/usr/bin/python3

import math


def makeChange(coins, total):
    coins.sort(reverse=True)
    rem = total
    solution = 0
    i = 0
    change = 0
    if not total:
        return 0
    while i < len(coins):
        j = i
        while j < len(coins):
            if coins[j] <= rem:
                change += math.floor(rem / coins[j])
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
