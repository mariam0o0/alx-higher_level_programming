#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    np = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            np += 1
        except IndexError:
            continue
    print()
    return np
