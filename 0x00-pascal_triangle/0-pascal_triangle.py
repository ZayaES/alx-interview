#!/usr/bin/python3
""" module for implementation of Pascal's triangle
"""


def pascal_triangle(n):
    """ creates a pascal trinagle
    """

    if n <= 0:
        return []

    pt = [0] * n

    for x in range(n):
        new_row = [0] * (x + 1)
        new_row[0] = 1
        new_row[-1] = 1

        for y in range(1, x):
            if y > 0 and y < len(new_row):
                a = pt[x - 1][y]
                b = pt[x - 1][y - 1]
                new_row[y] = a + b

        pt[x] = new_row

    return pt
