#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """Rotates a matrix by 90 degrees"""

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for rows in range(len(matrix)):
        matrix[rows] = matrix[rows][::-1]
