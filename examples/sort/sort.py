#!/usr/bin/python
"""Sort algorithms"""
# jshields

import logging
import copy

logging.basicConfig(filename='sort.log', format='%(asctime)s %(message)s', level=logging.DEBUG)


class Sort(object):
    """Sort class acts as a library for sorting algorithm methods"""

@classmethod
    def _quicksort_partition(cls, lst, start, end):
        """Internal partition and sorting method for Sort._quick driver method"""
        # the pivot element value will be the basis for comparison in sorting
        # we use the first item in this partition of the list as the pivot

        # this is the pivot value
        pivot = lst[start]
        # for now the pivot element remains in its initial list position,
        # and elements following it will be index swapped (their indices switch)
        # relative to the pivot value, not the pivot's index

        # set the starting positions of the left and right brackets
        left = start + 1
        right = end

        # keep swapping until the brackets pass/overlap each other
        swapping = True
        while swapping:
            # relative to the pivot value,
            # left bracket moves from left to right, and will trip on any element with a value not less than,
            # right bracket moves from right to left, and will trip on any element with a value not greater than
            while left <= right and lst[left] <= pivot:
                left = left + 1
            while lst[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                swapping = False
            else:
                # swap places if the bracket trips
                logging.debug('_quicksort_partition swapping: %s with %s' % (lst[left], lst[right]))
                tmp = lst[left]
                lst[left] = lst[right]
                lst[right] = tmp
        # swap pivot with the last known right bracket (greater than) element
        # this puts the pivot in between the elements that were swapped to the "less than" position
        # and elements that were swapped to the "greater than" position
        logging.debug('_quicksort_partition final swap: %s with %s' % (lst[start], lst[right]))
        tmp = lst[start]
        lst[start] = lst[right]
        lst[right] = tmp
        # the end result is that all elements less than are left of the pivot element, potentially unsorted
        # and all elements greater than the pivot element are right of the pivot element, potentially unsorted
        # return the pivot index, so that the less than and greater than sides can be partitioned and sorted again,
        # in Sort._quick
        logging.debug('pivot is %s' % right)
        return right

    @classmethod
    def _quick(cls, lst, start, end):
        """Quicksort implementation for a list, internal method"""
        # this method is called recursively
        # on the left and right sections of each partition
        # the sorting work is done in _quicksort_partition

        # eventually, a recursion depth will be reached
        # at which the overall list is fully sorted
        if start < end:
            # sort before and after the pivot
            pivot_index = cls._quicksort_partition(lst, start, end)
            cls._quick(lst, start, pivot_index - 1)
            cls._quick(lst, pivot_index + 1, end)
        return lst

    @classmethod
    def quick(cls, src_lst, start=0, end=None, inline=False):
        """
        Original C.A.R Hoare Quicksort partition scheme implementation
        https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
        """
        if end is None:
            end = (len(src_lst) - 1)

        # support for inline sorting vs returning a sorted copy
        if inline:
            lst = src_lst
        else:
            lst = copy.deepcopy(src_lst)
        return cls._quick(lst, start, end)

    @classmethod
    def _quicksort_partition2(cls, lst, left, right):
        """
        Internal partition and sorting method for Sort._quick driver method
        :param int left: start of partition
        :param int right: end of partition
        """
        # The pivot element value will be the basis for comparison in sorting.
        # We use the middle item in this partition of the list as the pivot,
        # to avoid O(n^2) performance in some common scenarios.
        # More discussion here:
        # https://stackoverflow.com/questions/164163/quicksort-choosing-the-pivot
        # https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot
        # "median of three" pivot selection is also good

        pivot_index = left + right // 2
        logging.debug('pivot index: %s' % pivot_index)

        pivot_value = lst[pivot_index]
        logging.debug('pivot value: %s' % pivot_value)

        # for now the pivot element remains in its initial list position,
        # and elements will be index swapped (their indices switch)
        # relative to the pivot value, not the pivot's index

        swapping = True
        while swapping:
            init_left = left
            init_right = right
            # with comparisons relative to the pivot,
            # "left pointer" index moves from left to right, and will stop on any element with a value not less than pivot value,
            # "right pointer" index moves from right to left, and will stop on any element with a value not greater than pivot value

            # if both "pointers" stopped, then swap the elements they stopped on?
            while left < right and lst[left] <= pivot_value:
                left = left + 1
            while right > left and lst[right] >= pivot_value:
                right = right - 1


            if right < left:  # stop condition?
                swapping = False
            else:
                # swap places if the "pointers" trip
                logging.debug('_quicksort_partition swapping: %s with %s' % (lst[left], lst[right]))
                tmp = lst[left]
                lst[left] = lst[right]
                lst[right] = tmp

        # the end result is that all elements "less than or equal" are left of the last position of the left bracket,
        # potentially unsorted
        # and all elements "greater than or equal" are right of the last position of the right bracket,
        # potentially unsorted

        # Edge case: all elements are less than/equal pivot, e.g.: [5, 3, 7, 1, 3, 2]
        # Result:

        # Edge case: all elements are the same
        # Result:

        # return an index such that the "less than" and "greater than" sides can be partitioned and sorted again
        # note that for this implementation, we do not split on the pivot

        return left

    @classmethod
    def _quick2(cls, lst, start, end):
        """Quicksort implementation for a list, internal method"""
        # this method is called recursively
        # on the left and right sections of each partition
        # the sorting work is done in _quicksort_partition

        # when we end up with a list of 1 item,
        # partitioning is done for that piece of the overall list
        if start < end:
            partition_index = cls._quicksort_partition(lst, start, end)

            # what do we do when partition_index is the start or end?

            logging.debug(
                'partition:',
                lst[start:partition_index],
                lst[partition_index+1, end]
            )
            cls._quick(lst, start, partition_index)
            cls._quick(lst, partition_index + 1, end)
        return lst

    @classmethod
    def quick2(cls, lst, start=0, end=None):
        """Quicksort implementation 2, middle pivot"""
        if end is None:
            end = (len(lst) - 1)
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

    @classmethod
    def selection(cls, lst):
        """
        TODO see if this works
        selection sort is a naive sorting algorithm
        Complexity:
        n + n-1 + n-2 ... 1
        "arithmetic series"
        Big O notation / approximation:
        O(n^2)
        """
        target_index = 0
        while target_index < len(lst) - 1:
            less_item = None
            less_item_index = None
            for i in range(target_index, len(lst) - 1):
                if less_item is None or item < less_item:
                    less_item = item
                    less_item_index = i
            else:
                # after list is consumed,
                # swap least value item we "selected" to the top
                tmp = lst[target_index]
                lst[target_index] = less_item
                lst[less_item_index] = tmp
                # next time through,
                # we can skip 1 slot since we know it contains previous least item
                target_index += 1
