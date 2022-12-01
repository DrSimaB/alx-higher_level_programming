#!/usr/bin/python3
import hidden_4
if _name_ == "_main_":
    for i in dir(hidden_4):
        if not i.startswith('_'):
            print(i)
