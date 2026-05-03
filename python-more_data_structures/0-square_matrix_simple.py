#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_num = []
        for num in row:
            new_num.append(num ** 2)
        new_matrix.append(new_num)
    return new_matrix
