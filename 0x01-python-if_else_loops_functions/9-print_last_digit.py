#!/usr/bin/python3
def print_last_digit(number):
    num = int(repr(number)[-1])
    print(num, end = "")
    return num
