#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # if a tuple has fewer than 2 elements, add 0s to it
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    # Take the first 2 elements of each tuple and add them
    result = (tuple_a[0]+ tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
