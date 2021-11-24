#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    count = 0
    for i in matrix:
        newMatrix.append([])
        for j in matrix[count]:
            newMatrix[count].append(j**2)
        count += 1
    return newMatrix
