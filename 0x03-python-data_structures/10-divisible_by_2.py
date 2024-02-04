#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for i in my_list:
        if i & 1:
            bool_list.append(False)
        else:
            bool_list.append(True)
    return bool_list
