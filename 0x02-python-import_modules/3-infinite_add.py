#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    nums = len(argv) - 1

    for i in range(1, nums + 1):
        sum += int(argv[i])
    print(sum)
