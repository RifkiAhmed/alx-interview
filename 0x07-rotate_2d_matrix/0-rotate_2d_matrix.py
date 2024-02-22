#!/usr/bin/python3
"""Rotate 2D matrix model
"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix
    """
    number_of_rows = len(matrix)
    for i in range(number_of_rows):
        for j in range(i, number_of_rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
