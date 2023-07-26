#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        tempList = []

        for j in range(i+1):
            if j == 0 or j == i:
                tempList.append(1)
            else:
                tempList.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(tempList)
    # print(triangle)
    return triangle
