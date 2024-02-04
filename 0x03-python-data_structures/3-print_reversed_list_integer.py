def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    reversed_list = my_list[::-1]
    for _ in reversed_list:
        print("{:d}".format(_))
