#!/usr/bin/python3
'''
Module to read and print a file
'''


def read_file(filename=""):
    ''' Reads file and prints it '''
    with open(filename) as file:
        for line in file:
            print(line.rstrip())
