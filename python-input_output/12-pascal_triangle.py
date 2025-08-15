#!/usr/bin/python3



def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]
            middle = [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)]
            triangle.append([1] + middle + [1])
    return triangle 


    