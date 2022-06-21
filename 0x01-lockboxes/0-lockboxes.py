#!/usr/bin/python3
"""
Module to solve a lockbox problem
"""


def canUnlockAll(boxes):
    """Function to unlock a set of locked boxes"""
    keys_set = {0}
    keys_set.update(boxes[0])
    present_keys = [] + boxes[0]

    for key in present_keys:
        if key < len(boxes) and key >= 0:
            keys_set.update(boxes[key])
        new_keys = keys_set - set(present_keys)
        present_keys += new_keys

    useful_keys = [k for k in keys_set if k < len(boxes)]
    if len(useful_keys) == len(boxes):
        return True
    return False
