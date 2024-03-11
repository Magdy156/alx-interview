#!/usr/bin/python3
"""
pascall's traingle problem
"""


def pascal_triangle(n):
    """return list of lists"""
    if n <= 0:
        return []
    result = [[1]]
    for i in range(n - 1):  # -1 becuase the result has already a list
        demo = []
        temp = result[-1].copy()
        temp.append(0)
        temp.insert(0, 0)
        for j in range(len(result[-1]) + 1):
            demo.append(temp[j] + temp[j + 1])
        result.append(demo)
    return result
