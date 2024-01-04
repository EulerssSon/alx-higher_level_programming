#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)

    if argv_len == 1:
        print("0 arguments.")
    else:
        if argv_len == 2:
            print("1 argument:")
        else:
            print(f"{argv_len - 1} arguments:")
        for i in range(1, argv_len):
            print(f"{i}: {argv[i]}")
