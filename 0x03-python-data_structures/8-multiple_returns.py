#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        first_ch = None
    else:
        first_ch = sentence[0]
    my_tuple = len(sentence), first_ch
    return (my_tuple)
