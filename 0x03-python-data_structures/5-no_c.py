#!/usr/bin/python3
def no_c(my_string):
    str = ''
    for i in my_string:
        if i not in ('c', 'C'):
            str += i
    return str
