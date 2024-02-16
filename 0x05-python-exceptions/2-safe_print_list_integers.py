#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    int_count = 0

    while (x > 0):
        try:
            print("{:d}".format(my_list[counter]), end="")
            int_count += 1
        except (IndexError) as err:
            raise err
        except (ValueError, TypeError):
            pass
        finally:
            counter += 1
            x -= 1
    print()
    return int_count
