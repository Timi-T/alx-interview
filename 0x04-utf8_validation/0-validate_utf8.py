#!/usr/bin/python3
"""
Module for utf-8 validation
"""


def validUTF8(data):
    """Function to validate an array of integers in utf-8"""

    for i in range(len(data)):
        # When integer is not in the range of valid integers
        if data[i] < 0 or data[i] > 255:
            return False
        # Convert each integer to its binary format
        bin_num = format(data[i], "b").zfill(8)
        # Get the first leading 1's
        byte_len = (bin_num.split('0', 1))[0]
        if byte_len:
            # Getting the length of the total bytes for the character
            byte_len = len(byte_len)
            if byte_len > 4:
                return False
            # If we have a length of byte beyond the length of the array
            if i + byte_len > len(data):
                return False
            # Getting the bytes/integers from the data array
            next_array = data[i + 1: byte_len + i]
            # Iterate through the new array representing the character
            for j in next_array:
                ch_bin = format(j, "b").zfill(8)
                if ch_bin[0] != "1" or ch_bin[1] != "0":
                    return False
                else:
                    return True
            i += byte_len
    return True
