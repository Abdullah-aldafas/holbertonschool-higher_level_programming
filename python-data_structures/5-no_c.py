#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for i in my_string:
        if i != "c" and i != "C":
            new = new + i
    return new
# return "".join([i for i in my_string if i != "c" and i != "C"])
