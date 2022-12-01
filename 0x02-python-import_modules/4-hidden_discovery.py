#!/usr/bin/python3

if _name_ == "_main_":
    import hidden_4
    for i in dir(hidden_4):
        if not i.startswith('_'):
            print(i)
