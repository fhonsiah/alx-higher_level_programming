#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        # Index is out of range, do nothing and return the original list
        return my_list
    else:
        # Slice the list to remove the item at the specified index
        return my_list[:idx] + my_list[idx+1:]
        # modify the original list in place
        my_list[:] = new_list
        # return the new list
        return new_list
