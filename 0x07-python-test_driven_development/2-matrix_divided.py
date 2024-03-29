#!/usr/bin/python3
"""
Module divide matrix
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(matrix[i]) != len(matrix[i + 1]) for i in range(len(matrix) - 1)):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return new_matrix
