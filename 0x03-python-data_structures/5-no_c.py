#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    if 'c' in my_list:
        my_list.remove('c')
    if 'C' in my_list:
        my_list.remove('C')
    return ''.join(my_list)
