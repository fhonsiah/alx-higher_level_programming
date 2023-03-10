#!/usr/bin/python3

def element_at(my_list, idx):
    """

    This function retrieves an element from a list like in C.

    Args:
        my_list: The list containing integers to be printed
        idx: The index to which the value is to be located.
    """
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    return my_list[idx]
