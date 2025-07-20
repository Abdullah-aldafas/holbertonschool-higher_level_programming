#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return 0
    elif idx > len(my_list):
        return null
    else:
        print(f"Element at index {idx} is {len(my_list) - 1}")
