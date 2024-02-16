#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    is_valid = False
    try:
        print("{:d}".format(value))
        is_valid = True
    except Exception as err:
        print("Exception:", err, file=stderr)
    finally:
        return is_valid
