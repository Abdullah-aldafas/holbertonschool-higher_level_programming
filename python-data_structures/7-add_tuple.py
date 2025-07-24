#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 1:
        a = tuple_a[0]
    else:
        a = 0
    if len(tuple_a) >= 2:
        b = tuple_a[1]
    else:
        b = 0
    if len(tuple_b) >= 1:
        i = tuple_b[0]
    else:
        i = 0
    if len(tuple_b) >= 2:
        c = tuple_b[1]
    else:
        c = 0

    r = a + i
    z = b + c
    return (r, z)
