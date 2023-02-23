#!/usr/bin/env python3
"""Task 0 module"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """ A function that checks whether the data given is a valid UTF8

    Args:
        data (List[int]): contains lists of integers to be checked

    Returns:
        bool: return true if the data is valid and false otherwise
    """
    byte_count = 0

    for i in data:
        if byte_count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
