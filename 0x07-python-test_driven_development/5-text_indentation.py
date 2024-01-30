#!/usr/bin/python3
"""
Module text_indentation
"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each of these characters: ., ? and :"""

    if text is None or not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if char in ['.', '?', ':']:
            print(char + '\n')
            flag = 1
        else:
            if flag == 0:
                print(char, end="")
            else:
                if char == ' ' or char == '\t':
                    pass
                else:
                    print(char, end="")
                    flag = 0
