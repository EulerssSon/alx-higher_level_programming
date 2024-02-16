#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0

    while (x > 0):
        try:
            print(my_list[counter], end="")
            counter += 1
            x -= 1
        except IndexError:
            break
    print()
    return counter
