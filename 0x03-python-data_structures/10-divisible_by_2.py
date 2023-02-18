#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    
    Returns a list of True or False values indicating whether each integer in my_list is a multiple of 2.

    :param my_list: A list of integers.
    :return: A list of True or False values.
    """

    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
