#!/usr/bin/python3
def no_c(my_string):
    list_of_string = list(my_string)
    for i in range(len(list_of_string)):
        if list_of_string[i] == "c" or list_of_string[i] == "C":
            list_of_string[i] = ""
    return "".join(list_of_string)
