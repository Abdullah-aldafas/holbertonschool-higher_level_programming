#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if sentence == "":
        f = None
    else:
        f = sentence[0]
    
    return (l , f)
