#!/usr/bin/python3
# 1-search_replace.py
# Benatha Simasiku


def search_replace(my_list, appearnace, replacer):
    """Replace all occurrences of an element by another in a new list."""
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == appearnace: #2 at main file
            new_list[i] = replacer #89 at main file
    return (new_list)
