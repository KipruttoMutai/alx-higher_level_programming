#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    for row in matrix:
        for item in row:
            if item != row[-1]:
                endspace = " "
            else:
                endspace = ""
            print("{:d}".format(item), end=endspace)
        print()
