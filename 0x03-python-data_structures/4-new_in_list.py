#!/usr/bin/python3
# 4-new_in_list.py

def element_at(my_list, idx):
    """Retrieve an element from a list."""
    if idx < 0 or idx >= len(my_list):
       return my_list[idx]

    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
