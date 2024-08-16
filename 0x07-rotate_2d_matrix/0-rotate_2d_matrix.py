#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """rotate matrix 90 degrees cw"""
    matrix.reverse()

    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
