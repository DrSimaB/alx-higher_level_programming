#!/usr/bin/python3
from sys import argv
if _name_ == "_main_":
    if len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(1, argv._getitem_(1)))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv._getitem_(i)))
    else:
        print("{} arguments.".format(len(argv) - 1))
