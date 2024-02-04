def no_c(my_string):
    list_of_string = list(my_string)
    for i in list_of_string:
        if i == 'c' or i == 'C':
            list_of_string.remove(i)
    return "".join(list_of_string)
