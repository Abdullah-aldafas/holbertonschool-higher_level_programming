#!/usr/bin/python3
def multiple_returns(sentence):
    le = len(sentence)
    if sentence == "":
        f = None
    else:
        f = sentence[0]
    return (le, f)
