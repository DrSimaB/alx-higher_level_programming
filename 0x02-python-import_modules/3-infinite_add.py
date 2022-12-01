#!/usr/bin/python3
if _name_ == "_main_":
    import sys
    count = len(argv)
    add = 0
    if count == 1:
        print("{}".format(add))
    else:
        for i in range(1, count):
            add += int(argv._getitem_(i))
        print("{}".format(add))
