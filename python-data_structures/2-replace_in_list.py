#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    list_copy = my_list
    list_copy[idx] = element
    return list_copy
