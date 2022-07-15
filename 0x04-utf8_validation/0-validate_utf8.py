#!/usr/bin/python3
"""
Module for utf-8 validation
"""


def validUTF8(data):
    """Function to validate an array of integers in utf-8"""
    i = 0
    while i < len(data):
        # Array element must be an integer
        if not isinstance(data[i], int):
            return False
        # Convert each integer to its binary format
        if data[i] >= 255:
            bin_num = format(data[i], "b")[-8:]
        else:
            bin_num = format(data[i], "b").zfill(8)
        if bin_num[0] == '1' and bin_num[1] == '0':
            return False
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
            i += byte_len
        else:
            i += 1
    return True
