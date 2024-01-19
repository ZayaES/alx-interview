#!/usr/bin/python3
"""contains function minOperations. see function for more detail"""


def minOperations(n):
    """finds the number of operations required to write
       the required number of H's.
    """

    cnt = 0
    pasted_chars = 1
    clip_b = 0

    while pasted_chars < n:
        if clip_b == 0:
            clip_b = pasted_chars
            cnt += 1

        if pasted_chars == 1:
            pasted_chars += clip_b
            cnt += 1
            continue

        remainder = n - pasted_chars
        if clip_b > remainder:
            return 0

        if remainder % pasted_chars != 0:
            pasted_chars += clip_b
            cnt += 1
        else:
            clip_b = pasted_chars
            pasted_chars += clip_b
            cnt += 2

    if pasted_chars == n:
        return cnt
    else:
        return 0
