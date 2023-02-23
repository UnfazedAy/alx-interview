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
    n_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        elif not (num & mask1 and not (num & mask2)):
            return False
        n_bytes -= 1
    return n_bytes == 0
