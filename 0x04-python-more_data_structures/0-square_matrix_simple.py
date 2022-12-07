#!/usr/bin/python3

def sqaure_matrix_simple(matrix=[]):
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
