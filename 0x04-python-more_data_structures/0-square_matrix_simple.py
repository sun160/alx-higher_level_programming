#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
   squared = []
    for num in matrix:
        squared.append([c**2 for c in num])
    return squared
