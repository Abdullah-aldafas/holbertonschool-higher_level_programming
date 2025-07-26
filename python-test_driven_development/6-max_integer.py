def max_integer(list=[]):
    """Returns the max integer in a list of integers"""
    if not isinstance(list, list):
        raise TypeError("list must be a list of integers")
    if len(list) == 0:
        return None
    result = list[0]
    for i in list:
        if i > result:
            result = i
    return result
