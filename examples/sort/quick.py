"""Some implementations of quicksort"""
import logging

logging.basicConfig(filename='quick_sort.log', format='%(asctime)s %(message)s', level=logging.DEBUG)


class QuickSort1(object):
    """Implementation 1: first element pivot"""

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
    def quick(cls, lst, start=0, end=None):
        """
        Original C.A.R Hoare Quicksort partition scheme implementation
        https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
        """
        if end is None:
            end = (len(lst) - 1)
        return cls._quick(lst, start, end)


class QuickSort2(object):
    """Implementation 2: middle pivot"""

    @classmethod
    def _quicksort_partition(cls, lst, left, right):
        """
        Internal partition and sorting method.
        The list is "virtually" partitioned using indices, not by making new list objects,
        so the operation is inline.
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
        logging.debug('left: %d, right: %d' % (left, right))

        pivot_index = left + right // 2  # <- should cause IndexError for certain data?
        # middle, but protection from integer overflow
        #pivot_index = left + (right-left) // 2
        logging.debug('pivot index: %s' % pivot_index)

        pivot_value = lst[pivot_index]
        logging.debug('pivot value: %s' % pivot_value)

        # for now the pivot element remains in its initial list position,
        # and elements will be index swapped (their indices switch)
        # relative to the pivot value

        while left < right:

            # with comparisons relative to the pivot,
            # "left pointer" index moves from left to right, and will stop on any element with a value not less than pivot value,
            # "right pointer" index moves from right to left, and will stop on any element with a value not greater than pivot value

            # if both "pointers" stopped, then swap the elements they stopped on?
            while lst[left] <= pivot_value:
                left += 1
            while lst[right] >= pivot_value:
                right -= 1

            if left < right:
                # swap
                logging.debug('before swap: ', lst)
                logging.debug('swapping: %s with %s' % (lst[left], lst[right]))
                tmp = lst[left]
                lst[left] = lst[right]
                lst[right] = tmp
                logging.debug('after swap: ', lst)

        # the end result is that all elements "less than or equal" are left of the last position of the left pointer,
        # potentially unsorted
        # and all elements "greater than or equal" are right of the last position of the right pointer,
        # potentially unsorted

        # Edge case: all elements are less than/equal pivot, e.g.: [5, 3, 7, 1, 3, 2]
        # Result:

        # Edge case: all elements are the same
        # Result:

        # return an index such that the "less than" and "greater than" sides can be partitioned and sorted again
        # note that for this implementation, we do not split on the pivot

        return left

    @classmethod
    def _quick(cls, lst, start, end):
        """
        Quicksort implementation for a list, internal method
        :param int start: lefthand bounds of list to be partitioned / sorted
        :param int end: righthand bounds of list to be partitioned / sorted
        """
        # this method is called recursively
        # on the left and right sections of each list partition
        # the sorting work is done in _quicksort_partition

        # when we end up with a list of 1 item,
        # we have partitioned and sorted as far as we can for this recursive depth
        if start < end:
            partition_index = cls._quicksort_partition(lst, start, end)

            logging.debug('partition: ', lst[start:partition_index], lst[partition_index+1, end])

            # possibly needs to be:
            #cls._quick(lst, start, last_right)
            #cls._quick(lst, last_left, end)

            cls._quick(lst, start, partition_index)
            cls._quick(lst, partition_index + 1, end)

        return lst

    @classmethod
    def quick(cls, lst, start=0, end=None):
        """
        Quicksort implementation 2,
        middle pivot selection
        """
        if end is None:
            end = (len(lst) - 1)
        logging.debug('start: ', lst)
        return cls._quick(lst, start, end)
