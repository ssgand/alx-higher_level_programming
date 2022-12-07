#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    y = []
    for i in range(len(matrix)):
        s = list(map(lambda x: x**2, matrix[i]))
        y.append(s)
    return y
