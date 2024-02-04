#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _ in matrix:
        for __ in _:
            print("{:d}".format(__), end=" ")
        print()
