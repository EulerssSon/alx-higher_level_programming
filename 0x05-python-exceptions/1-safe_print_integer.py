#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".form)
    except (ValueError, AttributeError):
        return False
    except Exception as e:
        return False
    else:
        return True
