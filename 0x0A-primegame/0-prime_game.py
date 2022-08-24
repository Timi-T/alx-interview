#!/usr/bin/python3
"""
Prime game DSA
"""


def isPrime(num):
    """Function to determine if a number is prime or not"""
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Function to determine the winner of a game"""
    if x > len(nums):
        return None
    Maria = 0
    Ben = 0
    for round in range(x):
        turn = 1
        options = [n + 1 for n in range(nums[round])]
        i = 1
        while i < len(options):
            if isPrime(options[i]):
                div = options[i]
                options.pop(i)
                j = 0
                while j < len(options):
                    if options[j] % div == 0:
                        options.pop(j)
                    j += 1
                turn += 1
                i = 0
            i += 1
        if turn % 2 == 0:
            Maria += 1
        else:
            Ben += 1
    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    else:
        return None
