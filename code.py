#!/usr/bin/python3
"""Passes pycodestyle"""


def do_add(self, s):
    my_list = s.split()
    if len(l) != 2:
        print("*** invalid number of arguments")
        return
    try:
        my_list = [int(i) for i in my_list]
    except ValueError:
        print("*** arguments should be numbers")
        return
    print(my_list[0]+my_list[1])
