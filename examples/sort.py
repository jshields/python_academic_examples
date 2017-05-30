#!/usr/bin/python
"""Sort algorithms"""
# jshields

import logging
import copy

logging.basicConfig(filename='sort.log', format='%(asctime)s %(message)s', level=logging.DEBUG)


class Sort(object):
    """Sort class acts as a library for sorting algorithm methods"""

    @classmethod
    def _quicksort_partition(cls, lst, left, right):
        """
        Internal partition and sorting method for Sort._quick driver method
        :param int left: start of partition
        :param int right: end of partition
        """
        # the pivot element value will be the basis for comparison in sorting
        # we use the middle item in this partition of the list as the pivot,
        # to avoid O(n^2) performance in some common scenarios
        # More discussion here:
        # https://stackoverflow.com/questions/164163/quicksort-choosing-the-pivot
        # https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot
        # "median of three" pivot selection is a good alternative

        # this is the pivot value
        pivot_index = left + right // 2
        pivot_value = lst[pivot_index]
        logging.debug('pivot is %s' % pivot_value)

        # for now the pivot element remains in its initial list position,
        # and elements will be index swapped (their indices switch)
        # relative to the pivot value, not the pivot's index

        # keep swapping until the brackets pass/overlap each other
        swapping = True
        while swapping:
            # with comparisons relative to the pivot,
            # left bracket index moves from left to right, and will stop on any element with a value not less than pivot value,
            # right bracket index moves from right to left, and will stop on any element with a value not greater than pivot value
            # if both brackets stopped without passing through each other, then swap the elements they stopped on
            while left < right and lst[left] <= pivot_value:
                left = left + 1
            while right > left and lst[right] >= pivot_value:
                right = right - 1

            if right <= left:
                # right reached left bracket, no values to swap were found
                swapping = False
            else:
                # swap places if the brackets trip
                logging.debug('_quicksort_partition swapping: %s with %s' % (lst[left], lst[right]))
                tmp = lst[left]
                lst[left] = lst[right]
                lst[right] = tmp

        # the end result is that all elements "less than" are left of the last position of the left bracket,
        # potentially unsorted
        # and all elements "greater than" are right of the last position of the right bracket,
        # potentially unsorted
        # return an index such that the "less than" and "greater than" sides can be partitioned and sorted again

        # right should equal left+1 at this point
        assert right == left+1

        # left and right should be the last positions of the "brackets"
        return left

    @classmethod
    def _quick(cls, lst, start, end):
        """Quicksort implementation for a list, internal method"""
        # this method is called recursively
        # on the left and right sections of each partition
        # the sorting work is done in _quicksort_partition

        # when we end up with a list of 1 item,
        # partitioning is done for that piece of the overall list
        if start < end:
            partition_index = cls._quicksort_partition(lst, start, end)
            logging.debug(
                'partition:',
                lst[start:partition_index],
                lst[partition_index+1, end]
            )
            cls._quick(lst, start, partition_index)
            cls._quick(lst, partition_index + 1, end)
        return lst

    @classmethod
    def quick(cls, src_lst, start=0, end=None, inline=False):
        """Quicksort implementation"""
        # this is a wrapper method to handle kwargs before starting the sort

        if end is None:
            end = (len(src_lst) - 1)

        # support for inline sorting vs returning a sorted copy
        if inline:
            lst = src_lst
        else:
            lst = copy.deepcopy(src_lst)
        return cls._quick(lst, start, end)

    @classmethod
    def _mergesort_merge(cls, start, end):
        """
        Merge two sorted halves of a list back together
        :param list start: list left half, already sorted
        :param list end: list right half, already sorted
        """
        leftside_end = (start + end) // 2
        rightside_start = leftside_end + 1
        # TODO


    @classmethod
    def _mergesort_recurse(cls, lst, start, end, tmp):
        # sorting is done when we reach a single list element to sort
        if start < end:
            _mergesort_recurse(lst, tmp, start, mid)
            _mergesort_recurse(lst, tmp, mid, end)
            _mergesort_merge(lst, tmp, start, end)

    @classmethod
    def merge(cls, lst):
        """
        Merge sort implementation

        Split the list in half, call merge sort on each half,
        then merge the sorted halves back together.

        Calling merge sort happens recursively.

        From the top frame's perspective, each list half is
        "magically" sorted and then they are merged back together such that the entire list will be sorted.
        Underneath, the list halves have the same thing done to them:
        they are split, sorted, and merged back together.
        So the "magic" sort when looking from the perspective of the most shallow recursive frame,
        is actually merge sort itself.

        On the lowest depth recursive frame,
        we end up with lists containing a single item,
        and that's when we stop calling merge sort / stop recursing.

        The splitting is done inline, by index,
        rather than creating new lists for each half, each time.
        """
        start = 0
        end = len(lst) - 1
        tmp = []
        _mergesort_recurse(lst, tmp, start, end)

    @classmethod
    def bubble(cls, lst):
        """Bubble sort implementation"""
        swapping = True
        while swapping:
            swapping = False
            # because we look-ahead by 1 index, only iterate to length - 1
            for i in range(len(lst) - 1):
                # bigger/greater items should "bubble" to the top
                # if one item belongs where the other is,
                # swap them as part of the sort
                if lst[i] > lst[i + 1]:
                    swapping = True
                    # swap the items
                    tmp = lst[i]
                    lst[i] = lst[i + 1]
                    lst[i + 1] = tmp
        return lst

    @classmethod
    def insertion(cls, src_lst, start=0, end=None, inline=False):
        """Insertion sort implementation"""
        # support for inline sorting vs returning a sorted copy
        if inline:
            lst = src_lst
        else:
            lst = copy.deepcopy(src_lst)

        if end is None:
            end = len(lst)

        # because we look-behind by 1 index, start iteration at length + 1
        for i in range(start + 1, end):
            value = lst[i]
            cursor = i - 1

            logging.debug(
                'insertion: for looping, index at %d, current value %s, cursor at %d' % (
                    i, value, cursor
                )
            )

            # while the elements behind the current element are of greater value,
            # push the current element backwards
            while lst[cursor] > value and cursor >= 0:
                # starting from the element of current 'value',
                # swap values with the element that the cursor is looking back towards,
                # falling through the rest of the list behind the current element
                logging.debug('insertion: while looping, shifting index of %s up by one' % lst[cursor])
                lst[cursor + 1] = lst[cursor]
                cursor -= 1
                logging.debug('insertion: while looping, cursor at %d' % cursor)
            # finally, insert the 'value' back into the list
            logging.debug('insertion: out of while, inserting %s back into the list at index %d' % (
                    lst[cursor + 1], cursor + 1
                )
            )
            lst[cursor + 1] = value

        return lst
