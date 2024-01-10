#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return list(map(lambda sub_matrix: list(map(lambda x: x**2, sub_matrix)), matrix))
