#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    """

    A function replaces and element in a list at a specific position without
    modifying the original list (like in C).

    Args:
        my_list: The list containing integers to be printed.
        idx: The index/position of the element to be replaced.
        new_element: The element to replace with.
    """
    if idx < 0:
        return my_list[:]
    elif idx > (len(my_list) - 1):
        return my_list[:]
    else:
        my_list_copy = my_list[:]
        my_list_copy[idx] = new_element
        return my_list_copy
