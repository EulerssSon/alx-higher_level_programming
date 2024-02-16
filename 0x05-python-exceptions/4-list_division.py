#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    counter = 0
    can_div_count = 0
    new_list = []
    while (list_length > 0):
        can_div = False
        try:
            x = my_list_1[counter] / my_list_2[counter]
            can_div_count += 1
            can_div = True
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            if not can_div:
                x = 0
        new_list.append(x)
        counter += 1
        list_length -= 1
    return new_list
