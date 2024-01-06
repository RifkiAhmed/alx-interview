#!/usr/bin/python3
''' Pascal's triangle '''


def pascal_triangle(n):
    '''
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    '''

    if (n <= 0):
        return []
    matrix = []
    for i in range(n):
        list = []
        for j in range(i + 1):
            if i == 0 or j == 0 or j == i:
                list.append(1)
            else:
                list.append(matrix[i - 1][j - 1] + matrix[i - 1][j])
        matrix.append(list)

    return matrix
