#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number,
    rounded to 2 decimal places.
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0 or div != div:  # div != div covers float('nan')
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float))
                for row in matrix for num in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
