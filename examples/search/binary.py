#!/usr/bin/python
"""Binary search algorithm"""
import logging


logging.basicConfig(
    filename='binary_search.log',
    format='%(asctime)s %(message)s',
    level=logging.DEBUG
)


def binary_search(item, lst):
    """
    Binary search for an item in an ordered list.
    Returns an index in the list or False if not found.

    :param item int: number to search for in the list.
    :param lst list: sorted list of ints, in ascending order.
    :return: index of item, or False if not found
    """
    bottom = 0
    top = len(lst) - 1
    while bottom <= top:
        middle = (bottom + top) // 2
        # middle, greater half or lesser half?
        if lst[middle] == item:
            # we found it
            return middle
        elif lst[middle] < item:
            # the item is greater than where we are looking
            # move the search bracket up
            bottom = middle + 1
        elif lst[middle] > item:
            # the item is less than where we are looking
            # move the search bracket down
            top = middle - 1

    return False
