#!/usr/bin/python3
"""
Module for pascal_triangle.
"""


def pascal_triangle(n):
    """ eturns a list of lists of integers
    representing the Pascal triangle of n """

    if n <= 0:
        return []

    Ptriangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = Ptriangle[i - 1][j - 1] + Ptriangle[i - 1][j]
        Ptriangle.append(row)

    return Ptriangle
