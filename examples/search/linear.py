#!/usr/bin/python
"""Linear search algorithm"""


def linear_search(item, lst):
    """
    Linear search of a list for an item.
    Returns the first index of the item in a list.
    Will return False if nothing is found.
    """
    pos = 0
    while pos < len(lst):
        if lst[pos] is item:
            return pos
        pos += 1
    # opted for False rather than -1,
    # because -1 can be used as a valid list index in python
    return False

    # real way to do this:
    # try:
    #    return lst.index(item)
    # except ValueError:
    #    return False
